# Phyllis Torres
# 17.2 Write an init Method for a Point Class Assignment
# Due 11/17/2016

print('17.2 Write an init Method for a Point Class Assignment \n')
print('Phyllis Torres\n\n')

print('This program will use a method that inits a Point class. ')


# create a point class
class Point:
    """Represents a point in a 2 dimensional space
    """

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


p = Point(3, 4)

print ('\nThe point defined is ' + str(p.x) + ', ' + str(p.y))


