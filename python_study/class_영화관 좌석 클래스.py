class MovieSeat:
    def __init__(self, seat_number):
        self.seat_number = seat_number
        self.reserved = False

    def reserve(self):
        if self.reserved:
            print("이미 예약된 좌석입니다.")
        else:
            self.reserved = True
            print("예약이 완료되었습니다.")

    def cancel(self):
        if self.reserved:
            self.reserved = False
            print("예약이 취소되었습니다.")
        else:
            print("예약된 좌석이 아닙니다.")

    def show_status(self):
        if self.reserved:
            status = "예약됨"
        else:
            status = "예약 가능"

        print(f"좌석 {self.seat_number}: {status}")


seat = MovieSeat("A-10")

seat.show_status()
seat.reserve()
seat.reserve()
seat.cancel()
seat.show_status()