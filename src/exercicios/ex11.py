# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum.


def sum_of_the_square() -> int:
    return sum(i**2 for i in range(1, 101))


def square_of_the_sum() -> int:
    return sum(range(1, 101)) ** 2
