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


#DB에 연결하고 조회결과를 읽을 수 있도록 설정한 뒤, 연결 객체를 돌려주는 함수
def get_database() -> sqlite3.Connection: # -> 는 반환형 힌트/실제 실행 동작을 만드는 것은 아님./ 이 함수가 끝날때 sqlite3.Connection 종류의 값을 돌려준다는 표시
    database = sqlite3.connect(DATABASE_PATH) # DB연결을 만듦/DATABASE_PATH는 앞에서 만든 DB파일 위치
    database.row_factory = sqlite3.Row #row는 DB에서 조회한 한 줄의 결과
    # row_factory = 포장 방식 설정 칸/ database의 조회 결과 포장 방식(row_factory)을 sqlite3.Row방식으로 설정
        # row_factory를 설정하지 않으면 조회 결과는 조회 순서만 있는 튜플
    # sqlite3.Row = “열 이름이 붙은 형태로 포장하라”는 포장 방식
    # .row_factory : 실제 객체에 들어있는 설정 이름이라 소문자
    # .Row : python클래스 이름이라 대문자로 시작
    return database


def initialize_database() -> None: # 데이터베이스를 초기 준비 한다는 의미(DB에 files, download_history표를 만드는 함수)
    """파일 정보와 다운로드 기록을 저장할 표를 한 번만 만듭니다.""" # 함수 설명운(docstring) : 설명하는 메모
    with get_database() as database: # 이전의 함수를 호출하여 DB연결을 만들고 database라고 명명
        # executescript()는 SQL명령이 여러 개가 담긴 긴 문자열을 한번에 실행
        # CREATE TABLE IF NOT EXISTS files : 표를 만드는데 이미 같은 이름의 표가 있으면 오류를 내지 말고 넘어간다.(이름 중복의 허용)
        # PRIMARY KEY : 각 행을 대표하는 고유값. 같은 id는 중복 저장이 안됨.
        # NOT NULL : 비어 있으면 안된다.
        # NOT NULL UNIQUE : 다른 행과 같은 값을 가질 수 없다.
        # upload_at : 업로드 시각
        # INTEGER : 정수, 즉 소수점 없는 숫자
        # DEFAULT 0 : 새 파일을 저장할 때 다운로드 횟수를 지정하지 않으면 자동으로 0부터 시작
        # download_history : 다운로드가 일어날 때마다 한 줄씩 쌓는 기록 표
        # integer primary key : 각 행을 구분하는 정수 id
        # AUTOINCREMENT : 새 기록이 추가될 대 SQLite가 id번호를 자동으로 증가(사용한 같은 번호를 다시 쓰지 않도록 만드는 옵션)
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


def is_txt_file(filename: str) -> bool: # 파일명이 TXT인지 확인하는 함수
    # filename: str 은 filename에는 글자(string)를 받아야 한다는 의미
    # -> bool : 결과는 True 또는 False라는 의미
    return filename.lower().endswith(".txt")
    # .endwith(".txt") : 파일 이름이 .txt 로 끝나는지 확인


def format_file_size(size_in_bytes: int) -> str: # 파일크기를 사람이 읽기 편한 글자로 바꾸는 함수
    if size_in_bytes < 1024: # 1.024KB보다 작으면 바이트 단위로 표시
        return f"{size_in_bytes} B"
    return f"{size_in_bytes / 1024:.1f} KB"
    # :.1f : 소수점 아래 한 자리까지 표시


def now_text() -> str: #DB에 저장하기 좋은 글자 형태로 만드는 함수
    # 서버가 실행되는 PC의 현재 시각을 기록합니다.
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    #datetime.now() : 서버 PC의 현재 날짜와 시각
    # .strftime() : 날짜와 시간을 원하는 글자형식으로 변환 ex) %Y : 연도 4자리, %H : 시(24시간제) 


initialize_database()


@app.get("/") # 사용자가 서버에 접속하면 index()를 실행한다는 의미
def index(): # 페이지의 첫 화면을 만드는 함수의 이름
    with get_database() as database:
        # files = database.execute(): files표에서 화면에 표시할 파일 정보를 모두 읽는다
        # ORDER BY : 정렬 기준 지정
        # uploaded_at : 업로드 시각으로 정렬
        # DESC : 최신 날짜부터 내림차순 정렬
        # .fetchall() : 조회된 모든 행을 가져온다
        files = database.execute(
            """
            SELECT original_name, output_name, sender_name, uploaded_at,
                   file_size, download_count
            FROM files
            ORDER BY uploaded_at DESC
            """
        ).fetchall()

    # 업로드 완료 메세지
    saved_name = request.args.get("saved") #request.args : url에 붙은 추가 정보
    message = "" # 빈 문자열로 만들고 아래의 if에서 saved_name이 있을 때만 성공 메세지를 넣는다
    if saved_name:
        # <p>는 HTML의 문단 태그/화면에 한 문단의 안내 문구를 만든다
        # class 'success'는 나중에 CSS에서 성공 메세지 색상을 지정하기 위해 붙인 것
        # escape(saved_name)은 파일명을 HTML에 안전하게 표시
        message = f"<p class='success'>변환 파일을 서버에 저장했습니다: {escape(saved_name)}</p>"

    if files: # files에 하나 이상의 파일이 있을 때만 표를 만든다
        # "".join(): 만들어진 여러 HTML 문자열을 빈 문자열 사이에 넣어 이어 붙임
        # <tr> : HTML표에서 한 줄을 뜻한다.
        # <td> : 표 안의 한 칸을 뜻한다.
        # <a> : 클릭할 수 있는 링크
        # href : 링크를 눌렀을 때 갈 주소
        # url_for('download', ) : download() 함수의 URL을 만듦
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
        #<table> : 표 전체
        #<thead> : 표 제목 줄
        #<th> : 제목 칸
        #<tbody> : 실제 데이터 줄
        #{file_rows} : python이 만든 파일 목록 HTML이 들어가는 자리
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
        file_list = "<p>아직 기록된 변환 파일이 없습니다.</p>" # 파일이 하나도 없으면 표 대신에 보여준다.

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
    # <form> : 사용자가 입력한 내용을 서버로 보내는 HTML구조
    # action = '/upload' : /upload 주소로 보냄
    # method = 'post' : post요청으로 보냄
    # entype = 'multipart/form-data' : 텍스트와 파일을 함께 전송하는 방식
    # id: <label for='sender_name'>과 연결해, “보낸 사람” 글자를 눌러도 입력칸에 커서가 가게 함
    # name='sender_name': 서버가 request.form.get("sender_name")으로 값을 찾는 이름
    # maxlength='100': 브라우저에서 최대 100자로 제한
    # placeholder: 비어 있을 때 보여 주는 안내 문구

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
