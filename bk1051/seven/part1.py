import numpy as np
import math

class ArrayShapeError(Exception):
	pass

def wrapped_array(start, end, columns, rows=None):
	'''Returns an array of consecutive integers wrapped
	across a certain number of columns.

	Note that end IS included in the array, unlike
	with np.arange().'''
	range_vector = np.arange(start, end+1)
	if rows is None:
		rows = math.ceil(float(range_vector.size)/columns)
	return np.resize(range_vector, (columns, rows)).T
	

def select_rows(array, rows):
	'''Returns specified rows of an array.

	array is a NumPy array.
	rows is an iterable

	Uses np.r_[], which is mentioned in
	"Tentative NumPy Tutorial"
	'''
	return array[rows, :]
	

def select_cols(array, cols):
	'''Returns specified columns of an array.

	array is a NumPy array.
	cols is an iterable

	Uses np.c_[], which is mentioned in
	"Tentative NumPy Tutorial"
	
	'''
	return array[:, cols]


def select(array, start, end):
	'''Returns a rectangular portion of an array.

	array is a NumPy array.
	start is a tuple/list with the coordinates for the
		upper left of the rectangular portion
	end is a tuple/list with the coordinates for the
		lower right of the rectangular portion
	'''
	return array[start[0]:end[0]+1, start[1]:end[1]+1]


def filter_array(array, function):
	'''Returns an array where each value is filtered.

	For each value in the array, the value is passed
	to function. If the result is True, the value is 
	included in the final array. If it is false, it is
	replaced with missing (None)
	'''
	# Create an array of same shape as array, but all missing
	result = np.empty(array.shape, dtype='bool')
	missing = np.empty(array.shape).fill(np.nan)

	for r, row in enumerate(array):
		for c, value in enumerate(row):
			result[r, c] = function(value)

	# np.where replaces the np.nan values in missing with None
	return np.where(result, array, missing)

def question_1a(array):
	print select_rows(array, (1, 3))

def question_1b(array):
	print select_cols(array, [1])

def question_1c(array):
	print select(array, (1, 0), (3, 2))

def question_1d(array):
	print filter_array(array, lambda x: 3 <= x <= 11)

def run():
	array = wrapped_array(1, 15, 3)
	print array
	question_1a(array)
	question_1b(array)
	question_1c(array)
	question_1d(array)
		








