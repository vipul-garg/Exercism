"""
Differences of Squares : Find the difference between the 
square of the sum and the sum of the squares of the first N natural numbers
"""
def square_of_sum(number):
    """
    square of the sum of the first N natural numbers
    :param number: The number to test.
    :return: The square of the sum of the first N natural numbers
    """
    return sum(range(1, number + 1)) ** 2


def sum_of_squares(number):
    """
    sum of the squares of the first N natural numbers
    :param number: The number to test.
    :return: The sum of the squares of the first N natural numbers
    """
    return sum(i ** 2 for i in range(1, number + 1))


def difference_of_squares(number):
    """
    difference between the 
    square of the sum and the sum of the squares of the first N natural numbers
    :param number: The number to test.
    :return: The difference between the square of the sum and the sum of the squares of the first N natural numbers
    """
    return square_of_sum(number) - sum_of_squares(number)
