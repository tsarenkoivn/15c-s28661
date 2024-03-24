
class SquareGenerator:
    def squares(self, start, end):
        if end < start:
            raise ValueError("End of the range cannot be less than the start.")

        return [x ** 2 for x in range(start, end + 1)]