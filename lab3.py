import math

# task1
numlist = [x ** 2 for x in range(11)]
print(numlist)


# task2
def e_squares(start, end):
    return [x ** 2 for x in range(start, end + 1)]


print(e_squares(2, 10))


# task3

class SquareGenerator:
    def squares(self, start, end):
        return [x ** 2 for x in range(start, end + 1)]


a = SquareGenerator()
print(a.squares(3, 10))


# task4

rootlist = [math.sqrt(x) for x in a.squares(1, 10)]
print(rootlist)