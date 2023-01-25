"""
Raindrops
"""
def convert(number):
    """
    Convert a number to a string, the contents of which depend on the number's factors.
    If the number has 3 as a factor, output 'Pling'.
    If the number has 5 as a factor, output 'Plang'.
    If the number has 7 as a factor, output 'Plong'.
    """
    raindropSound =""
    if number%3==0:
        raindropSound+="Pling"
    if number%5==0:
        raindropSound+="Plang"
    if number%7==0:
        raindropSound+="Plong"
    if raindropSound=="": 
        raindropSound=str(number)
    return raindropSound
