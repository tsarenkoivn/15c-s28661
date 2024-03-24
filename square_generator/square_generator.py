
class SquareGenerator:
    def squares(self, start, end):
        if end < start:
            print("end cannot be less than start")

        return [x ** 2 for x in range(start, end + 1)]