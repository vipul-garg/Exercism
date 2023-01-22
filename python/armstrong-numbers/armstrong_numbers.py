"""
Determine whether a given number is an Armstrong number.
"""
def is_armstrong_number(number):
    """
    Return a boolean value indicating whether the given number is an Armstrong number.
    :param number: The number to test.
    :return: True if the number is an Armstrong number, False otherwise.
    """
    digits = [int(d) for d in str(number)]
    return sum(digit ** len(digits) for digit in digits) == number
