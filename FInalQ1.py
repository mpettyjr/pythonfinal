"""This program will take radius from user input and will calculate area, diameter, or perimeter of circle.
Program uses 'pi' import from math.
"""
from math import pi

def circle():
    """Function will prompt user to choose area, diameter, or perimeter options.
    Function uses 'pi' import and returns calculated answer.
    """
    option = input('For which you would like to calculate? (type \'a\' for area, \'d\': diameter, or \'c\' circumference): ')
    if option == 'a':
        r = int(input('Input the radius: '))
        print(pi * r**2)
    elif option == 'd':
        r = int(input('Input the radius: '))
        print(2 * r)
    elif option == 'c':
        r = input('Input the radius ')
        print(2 * pi * float(r))
circle()

