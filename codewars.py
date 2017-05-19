import math
from math import sqrt

'''Implement a method that accepts 3 integer values a, b, c. 
   The method should return true if a triangle can be built 
   with the sides of given length and false in any other case.'''

def is_triangle(a, b, c):
	inputs = sorted([a, b, c])
	if (inputs[0] + inputs[1]) <= inputs[2]:
		return True
	else:
		return False

'''In this kata, you are asked to square every digit of a number.
   If we run 9119 through the function, 811181 will come out.'''

def square_digits(num):
	# ret = ""
    # for x in str(num):
    #     ret += str(int(x)**2)
    # return int(ret)
	joined = lambda squared_list: int(''.join(str(i) for i in squared_list))
	return joined([int(i)**2 for i in str(num)])

''' '''