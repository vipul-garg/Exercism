"""
Collatz Conjecture
"""
def steps(number):
    """
    Take any positive integer n.
    If n is even, divide n by 2 to get n / 2.
    If n is odd, multiply n by 3 and add 1 to get 3n + 1.
    Repeat the process indefinitely.
    The conjecture states that no matter which number you start with, you will always reach 1 eventually.
    Given a number n, return the number of steps required to reach 1.
    :param number: int
    :return: int
    """
    steps_to_1 = 0
    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    while number != 1:
        if number % 2 == 0:
            number = number / 2
        else:
            number = 3 * number + 1
        steps_to_1 += 1
    return steps_to_1
