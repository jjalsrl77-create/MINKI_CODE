class MovieTheater:
    def __init__(self, movie_title, total_seats):
        self.movie_title = movie_title
        self.total_seats = total_seats
        self.reserved_seats = []

    def reserve(self, seat_number):
        if seat_number < 1 or seat_number > self.total_seats:
            raise ValueError("올바르지 않은 좌석 번호입니다.")

        if seat_number in self.reserved_seats:
            raise ValueError("이미 예약된 좌석입니다.")

        self.reserved_seats.append(seat_number)

    def cancel(self, seat_number):
        if seat_number not in self.reserved_seats:
            raise ValueError("예약되지 않은 좌석입니다.")

        self.reserved_seats.remove(seat_number)

    def get_available_seats(self):
        available_seats = []

        for seat_number in range(1, self.total_seats + 1):
            if seat_number not in self.reserved_seats:
                available_seats.append(seat_number)

        return available_seats

    def get_reserved_count(self):
        return len(self.reserved_seats)

    def __str__(self):
        return (
            f"{self.movie_title} | "
            f"전체 {self.total_seats}석 | "
            f"예약 {self.get_reserved_count()}석"
        )

theater = MovieTheater("인터스텔라", 5)

theater.reserve(2)
theater.reserve(4)

print(theater)
print(theater.get_available_seats())

theater.cancel(2)

print(theater.get_available_seats())