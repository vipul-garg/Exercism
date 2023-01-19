"""
Leap Year Exercise on Exercism.io
"""
def leap_year(year):
    """
    Returns True if the year is a leap year, False otherwise.
    When is it a Leap Year as per the Georgian Calendar?
    on every year that is evenly divisible by 4
    except every year that is evenly divisible by 100
    unless the year is also evenly divisible by 400
    
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False
