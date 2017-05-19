from math import sqrt

'''Implement a method that accepts 3 integer values a, b, c. 
   The method should return true if a triangle can be built 
   with the sides of given length and false in any other case.'''

def is_triangle(a, b, c):
    sur = (a + b + c) / 2
    area = (sur * (sur - a) * (sur - b) * (sur- c))**0.5
    if area > 0:
        return True
    else:
        return False
