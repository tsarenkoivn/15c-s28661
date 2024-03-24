# task1
numlist = [x ** 2 for x in range(11)]
print(numlist)


# task2
def e_squares(start, end):
    squarelist = [x ** 2 for x in range(start, end + 1)]
    return squarelist


print(e_squares(2, 10))
