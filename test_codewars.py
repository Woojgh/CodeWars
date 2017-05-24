import pytest

PARAMS_TABLE_TRIANGLE = [
	(1,2,3, True),
	(2,3,3, False),
	(2,1,6, True)
]
PARAMS_TABLE_SQUARE = [
	(9119, 811181)
]
PARAMS_TABLE_DNA = [
	('GTAT', 'CATA')
]
PARAMS_TABLE_IQ = [
	('2 4 7 8 10', 3)
]
PARAMS_TABLE_FIND = [
	([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5], 5)
]
PARAMS_TABLE_COMP = [
	([121, 144, 19, 161, 19, 144, 19, 11], [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19], True)
]
PARAMS_TABLE_VALIDATE = [
	(1234, True)
]
@pytest.mark.parametrize('a,b,c, result', PARAMS_TABLE_TRIANGLE)
def test_is_triangle(a,b,c, result):
	from codewars import is_triangle
	assert is_triangle(a,b,c) == result

@pytest.mark.parametrize('num, result', PARAMS_TABLE_SQUARE)
def test_square_digits(num, result):
	from codewars import square_digits
	assert square_digits(num) == result

@pytest.mark.parametrize('dna, result', PARAMS_TABLE_DNA)
def test_dna_strand(dna, result):
	from codewars import DNA_strand
	assert DNA_strand(dna) == result

@pytest.mark.parametrize('numbers, result', PARAMS_TABLE_IQ)
def test_iq(numbers, result):
	from codewars import iq_test
	assert iq_test(numbers) == result

@pytest.mark.parametrize('seq, result', PARAMS_TABLE_FIND)
def test_find_it(seq, result):
	from codewars import find_it
	assert find_it(seq) == result

@pytest.mark.parametrize('array1,array2, result', PARAMS_TABLE_COMP)
def test_comp(array1, array2, result):
	from codewars import comp
	assert comp(array1, array2) == result
	
@pytest.mark.parametrize('pin, result', PARAMS_TABLE_VALIDATE)
def test_validate_pin(pin, result):
	from codewars import validate_pin
	assert validate_pin(pin) == result
