'''
Write a program that calculates the number of grains of wheat on a chessboard
'''
def square(number):
    """
    Returns the number of grains of wheat on a given square
    The number of grains doubles on each square
    :param number: the square number
    """
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    else:
        return 2 ** (number - 1)


def total():
    """
    Returns the total number of grains of wheat on the chessboard
    """
    count = 0
    for i in range(0,64):
        count += 2**i
    return count
