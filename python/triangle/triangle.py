'''
Write a program that can tell you if a triangle is equilateral, isosceles, or scalene.
'''

def equilateral(sides):
    """
    An equilateral triangle has all three sides the same length.
    :param sides: a list of three integers
    :return: True if the triangle is equilateral, False otherwise
    """
    isEquilateral = False
    if isTriangle(sides) and (sides[0] == sides[1] == sides[2]):
        isEquilateral = True
    return isEquilateral

def isosceles(sides):
    """
    An isosceles triangle has at least two sides the same length.
    :param sides: a list of three integers
    :return: True if the triangle is isosceles, False otherwise
    """
    isIsoceles = False
    if isTriangle(sides) and (sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2]):
        isIsoceles = True
    return isIsoceles


def scalene(sides):
    """
    A scalene triangle has all sides of different lengths.
    :param sides: a list of three integers
    :return: True if the triangle is scalene, False otherwise
    """
    isScalene = False
    if isTriangle(sides) and (sides[0] != sides[1] and sides[1] != sides[2] and sides[0] != sides[2]):
        isScalene = True
    return isScalene

def isTriangle(sides):
    """
    A triangle is a polygon with three edges and three vertices.
    :param sides: a list of three integers
    :return: True if the triangle is a triangle, False otherwise
    """
    isTriangle = False
    if sides[0] + sides[1] > sides[2] and sides[1] + sides[2] > sides[0] and sides[0] + sides[2] > sides[1]:
        isTriangle = True
    return isTriangle
    