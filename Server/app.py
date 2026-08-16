from datetime import datetime
from html import escape
from pathlib import Path
import sqlite3
from uuid import uuid4

from flask import Flask, abort, redirect, request, send_from_directory, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)

# 서버 PC에 원본과 변환 결과를 보관할 폴더입니다.
BASE_DIR = Path(__file__).resolve().parent
UPLOAD_DIR = BASE_DIR / "uploads"
OUTPUT_DIR = BASE_DIR / "outputs"
DATABASE_PATH = BASE_DIR / "transfer_history.db"
UPLOAD_DIR.mkdir(exist_ok=True)
OUTPUT_DIR.mkdir(exist_ok=True)

# 실습용 서버가 너무 큰 파일을 받지 않도록 1 MB로 제한합니다.
app.config["MAX_CONTENT_LENGTH"] = 1 * 1024 * 1024


def get_database() -> sqlite3.Connection:
    database = sqlite3.connect(DATABASE_PATH)
    database.row_factory = sqlite3.Row
    return database


def initialize_database() -> None:
    """파일 정보와 다운로드 기록을 저장할 표를 한 번만 만듭니다."""
    with get_database() as database:
        database.executescript(
            """
            CREATE TABLE IF NOT EXISTS files (
                id TEXT PRIMARY KEY,
                original_name TEXT NOT NULL,
                output_name TEXT NOT NULL UNIQUE,
                sender_name TEXT NOT NULL,
                uploaded_at TEXT NOT NULL,
                file_size INTEGER NOT NULL,
                download_count INTEGER NOT NULL DEFAULT 0
            );

            CREATE TABLE IF NOT EXISTS download_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                file_id TEXT NOT NULL,
                downloaded_at TEXT NOT NULL,
                downloader_ip TEXT,
                FOREIGN KEY (file_id) REFERENCES files(id)
            );
            """
        )


def is_txt_file(filename: str) -> bool:
    return filename.lower().endswith(".txt")


def format_file_size(size_in_bytes: int) -> str:
    if size_in_bytes < 1024:
        return f"{size_in_bytes} B"
    return f"{size_in_bytes / 1024:.1f} KB"


def now_text() -> str:
    # 서버가 실행되는 PC의 현재 시각을 기록합니다.
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


initialize_database()


@app.get("/")
def index():
    with get_database() as database:
        files = database.execute(
            """
            SELECT original_name, output_name, sender_name, uploaded_at,
                   file_size, download_count
            FROM files
            ORDER BY uploaded_at DESC
            """
        ).fetchall()

    saved_name = request.args.get("saved")
    message = ""
    if saved_name:
        message = f"<p class='success'>변환 파일을 서버에 저장했습니다: {escape(saved_name)}</p>"

    if files:
        file_rows = "".join(
            "<tr>"
            f"<td><a href='{url_for('download', filename=file['output_name'])}'>"
            f"{escape(file['original_name'])}</a></td>"
            f"<td>{escape(file['sender_name'])}</td>"
            f"<td>{escape(file['uploaded_at'])}</td>"
            f"<td>{format_file_size(file['file_size'])}</td>"
            f"<td>{file['download_count']}</td>"
            "</tr>"
            for file in files
        )
        file_list = f"""
        <table>
            <thead>
                <tr><th>변환 파일</th><th>보낸 사람</th><th>업로드 날짜</th>
                    <th>파일 크기</th><th>다운로드 수</th></tr>
            </thead>
            <tbody>{file_rows}</tbody>
        </table>
        """
    else:
        file_list = "<p>아직 기록된 변환 파일이 없습니다.</p>"

    return f"""
    <!doctype html>
    <html lang='ko'>
    <meta charset='utf-8'>
    <title>텍스트 대문자 변환 서버</title>
    <style>
        body {{ font-family: sans-serif; max-width: 900px; margin: 40px auto; padding: 0 16px; }}
        label {{ display: block; margin: 12px 0 4px; }}
        input, button {{ padding: 8px; }}
        table {{ border-collapse: collapse; width: 100%; margin-top: 12px; }}
        th, td {{ border: 1px solid #ccc; padding: 9px; text-align: left; }}
        th {{ background: #f3f3f3; }}
        .success {{ color: #176b32; }}
    </style>
    <body>
        <h1>텍스트 대문자 변환 서버</h1>
        <p>TXT 파일을 올리면 서버가 변환한 결과를 보관합니다.</p>
        <form action='/upload' method='post' enctype='multipart/form-data'>
            <label for='sender_name'>보낸 사람</label>
            <input id='sender_name' name='sender_name' maxlength='100' placeholder='비워 두면 익명'>
            <label for='file'>TXT 파일</label>
            <input id='file' type='file' name='file' accept='.txt,text/plain' required>
            <button type='submit'>서버에 업로드하고 변환</button>
        </form>
        {message}
        <h2>서버에 저장된 변환 파일</h2>
        {file_list}
    </body>
    </html>
    """


@app.post("/upload")
def upload():
    uploaded_file = request.files.get("file")
    sender_name = (request.form.get("sender_name") or "").strip()

    if len(sender_name) > 100:
        return "보낸 사람 이름은 100자 이하여야 합니다.", 400
    if not uploaded_file or not uploaded_file.filename:
        return "파일을 선택하세요.", 400
    if not is_txt_file(uploaded_file.filename):
        return "TXT 파일만 업로드할 수 있습니다.", 400

    # 이름을 쓰지 않아도 파일을 올릴 수 있게 기본 표시 이름을 사용합니다.
    sender_name = sender_name or "익명"

    original_name = secure_filename(uploaded_file.filename) or "input.txt"
    file_id = uuid4().hex
    raw_data = uploaded_file.read()

    try:
        text = raw_data.decode("utf-8-sig")
    except UnicodeDecodeError:
        return "UTF-8 형식의 텍스트 파일만 지원합니다.", 400

    # 원본과 변환 결과 모두 서버 PC의 폴더에 저장합니다.
    (UPLOAD_DIR / f"{file_id}_{original_name}").write_bytes(raw_data)
    output_name = f"converted_{file_id}_{original_name}"
    (OUTPUT_DIR / output_name).write_bytes(text.upper().encode("utf-8"))

    # 파일 목록에 보일 정보와 이후의 다운로드 기록을 데이터베이스에 남깁니다.
    with get_database() as database:
        database.execute(
            """
            INSERT INTO files (
                id, original_name, output_name, sender_name, uploaded_at, file_size
            ) VALUES (?, ?, ?, ?, ?, ?)
            """,
            (file_id, uploaded_file.filename, output_name, sender_name, now_text(), len(raw_data)),
        )

    return redirect(url_for("index", saved=output_name))


@app.get("/download/<filename>")
def download(filename):
    # 데이터베이스에 등록된 파일만 내려받게 하고, 다운로드 사실을 함께 기록합니다.
    with get_database() as database:
        file = database.execute(
            "SELECT id, original_name FROM files WHERE output_name = ?", (filename,)
        ).fetchone()
        if file is None:
            abort(404)

        database.execute(
            "UPDATE files SET download_count = download_count + 1 WHERE id = ?",
            (file["id"],),
        )
        database.execute(
            """
            INSERT INTO download_history (file_id, downloaded_at, downloader_ip)
            VALUES (?, ?, ?)
            """,
            (file["id"], now_text(), request.remote_addr),
        )

    # 서버 내부 저장명에는 충돌 방지용 ID를 유지하되, 받는 사람에게는
    # ID를 뺀 알아보기 쉬운 이름으로 내려보냅니다.
    download_name = f"converted_{secure_filename(file['original_name']) or 'input.txt'}"
    return send_from_directory(
        OUTPUT_DIR,
        filename,
        as_attachment=True,
        download_name=download_name,
    )


@app.errorhandler(413)
def file_too_large(error):
    return "파일 크기는 1MB 이하여야 합니다.", 413


if __name__ == "__main__":
    # 다른 PC가 접속할 수 있도록 모든 네트워크 인터페이스에서 수신합니다.
    app.run(host="0.0.0.0", port=5000, debug=False)
