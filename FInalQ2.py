"""This program will include the 'math' import to 
1. calculate the hypotenuse of a right triangle
2. find the 2 other missing angles associated with the given lengths
"""

import math

def missing_landas():
    """Function missing_landas() will 
    1. prompt user for sides left and right of 90degree angle
    2. use math.hypot() to calculate the hypotenuse of the triangle
    3. use math.radians() to convert 90degrees to radians for use in math.cos() to calculate smaller of three angles
    4. subtracts small angle and 90degree from 180 t find missing angle
    """
    hypot = 0
    angle = 90
    l = int(input('Input first length (side length can be 1-20: '))
    r = int(input('Input second length (side length can be 1-20: '))
    if (l >= 1 and l <= 20) and (r >= 1 and r <= 20):
        hypot = math.hypot(l, r)
        a = math.cos(math.radians(angle))
        smaller_angle = (math.sin(math.radians(angle)) * 5) / hypot
        smaller_angle = math.asin(smaller_angle)
        smaller_angle = math.degrees(smaller_angle)
        langle = 180 - angle - smaller_angle
        print('Hypotenuse: {:.2f}, Smaller Angle: {:.2f}, Last Angle: {:.2f}'.format(hypot, smaller_angle, langle))
    else:
        print('You have entered incorrect side values. Please try again')
        missing_landas()

missing_landas()