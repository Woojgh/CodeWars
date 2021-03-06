import math
import functools
from functools import reduce
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
   If we run 9119 through the function, 811181 will come out. 7kyu'''

def square_digits(num):
	squared = ''.join([str(int(i)**2) for i in str(num)])
	return int(squared)

'''In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G".
   You have function with one side of the DNA; you need to get the other complementary side.
   DNA strand is never empty or there is no DNA at all . 7kyu'''
def DNA_strand(dna):
	strands_base = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
	given_dna = list(dna)
	return ''.join([strands_base[strand] for strand in given_dna])
	# Test.assert_equals(DNA_strand("GTAT"),"CATA","String GTAT is")

'''needs a program that among the given numbers finds one that is different in evenness, 
   and return a position of this number. 6kyu'''
def iq_test(numbers):
    temp = []
    new_list = numbers.split()
    for digit in new_list:
      test_number = int(digit) % 2
      temp.append(test_number)
    if temp.count(0) > temp.count(1):
      return temp.index(1) + 1
    else:
      return temp.index(0) + 1
	# for i in [i for i,x in enumerate(str(numbers)) if x == 1]:
	# 	print(i)
'''Given an array, find the int that appears an odd number of times. 6kyu'''
def find_it(seq):
	return reduce(lambda x, y: x^y, seq)
# test.assert_equals(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]), 5)

'''write a function that checks whether the two arrays have the "same" elements and multiplicities. 6kyu'''
def comp(array1, array2):
	try:
		return sorted([i ** 2 for i in array1]) == sorted(array2)
	except:
		return False


'''ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.
   If the function is passed a valid PIN string, return true, else return false.'''
def validate_pin(pin):
	if len(str(pin)) == 4 or len(str(pin)) == 6:
		return True
	else:
		return False
# Test.assert_equals(validate_pin("1"),False, "Wrong output for '1'")
# Test.assert_equals(validate_pin("12"),False, "Wrong output for '12'")
''''''




	