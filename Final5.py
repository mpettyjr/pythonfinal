"""This program creates a class called 'Rectangle' that includes two functions area() and perimeter().
User will choose which function to call. Each function will allow user to input length or coordinates 
as variables for calculation.
"""

class Rectangle:
    def area(self):
        """Function area() will allow the user to calculate the area by inputting the lengths or coordinates of a rectangle."""
        option = input('Lengths or coordinate points? \'l\' for lengths, \'c\' for coordinates')
        if option == 'l':
            x = int(input('Input length1: '))
            y = int(input('Input length2: '))
            return x * y
        elif option == 'c':
            point1 = input('Input top-left coordinate (x y): ')
            point_1 = point1.split(' ')
            first_points = []
            for i in point_1:
                first_points.append(int(i))
            point2 = input('Input bottom-right coordinate (x y): ')
            point_2 = point2.split(' ')
            second_points = []
            for i in point_2:
                second_points.append(int(i))
            area = (second_points[0] - first_points[0]) * (first_points[1] - second_points[1])
            return area

    def perimeter(self):
        """Function perimeter() will allow the user to calculate the perimeter by inputting the lengths or coordinates of a rectangle."""
        option = input('Lengths or coordinate points? \'l\' for lengths, \'c\' for coordinates')
        if option == 'l':
            x = int(input('Input length1: '))
            y = int(input('Input length2: '))
            return 2 * (x + y)
        elif option == 'c':
            point1 = input('Input top-left coordinate (x y): ')
            point_1 = point1.split(' ')
            first_points = []
            for i in point_1:
                first_points.append(int(i))
            point2 = input('Input bottom-right coordinate (x y): ')
            point_2 = point2.split(' ')
            second_points = []
            for i in point_2:
                second_points.append(int(i))
            perim = (second_points[0] - first_points[0]) + (first_points[1] - second_points[1])
            return 2 * perim


option = input('Would you like to calculate the perimeter or area of your rectangle? \'a\' for area, \'p\' for perimeter')
if option == 'a':
    x = Rectangle()
    print(x.area())
elif option == 'p':
    x = Rectangle()
    print(x.perimeter())
else:
    print('You have selected an incorrect option.')



