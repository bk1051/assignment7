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
	'''
	pass

def select_cols(array, cols):
	'''Returns specified columns of an array.

	array is a NumPy array.
	cols is an iterable
	'''
	pass

def select(array, start, end):
	'''Returns a rectangular portion of an array.

	array is a NumPy array.
	start is a tuple/list with the coordinates for the
		upper left of the rectangular portion
	end is a tuple/list with the coordinates for the
		lower right of the rectangular portion
	'''
	pass

def filter(array, function):
	'''Returns an array where each value is filtered.

	For each value in the array, the value is passed
	to function. If the result is True, the value is 
	included in the final array. If it is false, it is
	replaced with missing (np.nan)
	'''
	pass
