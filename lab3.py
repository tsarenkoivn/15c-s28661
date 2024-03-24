import math
from square_generator.square_generator import SquareGenerator

# task1
numlist = [x ** 2 for x in range(11)]
print(numlist)


# task2
def e_squares(start, end):
    return [x ** 2 for x in range(start, end + 1)]


print(e_squares(2, 10))



a = SquareGenerator()
print(a.squares(3, 10))


# task4

rootlist = [math.sqrt(x) for x in a.squares(1, 10)]
print(rootlist)


# task5
a.squares(10, 1)


# task 8
class CubicGenerator(SquareGenerator):
    def squares(self, start, end):
        if end < start:
            raise ValueError("End of the range cannot be less than the start.")

        return [x ** 2 for x in range(start, end + 1)]

    def cubes(self, start, end):
        if end < start:
            raise ValueError("End of the range cannot be less than start")

        return [x**3 for x in range(start, end + 1)]

c = CubicGenerator()
print(c.cubes(1, 10))
print(c.squares(100, 1))