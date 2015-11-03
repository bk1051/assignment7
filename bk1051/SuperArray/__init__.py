from SuperArray import *
import math

'''Factory methods'''


def wrapped_array(start, end, columns, rows=None):
	'''Returns an array of consecutive integers wrapped
	across a certain number of columns.

	Note that end IS included in the array, unlike
	with np.arange().'''
	range_vector = np.arange(start, end+1)
	if rows is None:
		rows = math.ceil(float(range_vector.size)/columns)
	return np.resize(range_vector, (columns, rows)).T.view(SuperArray)
