import numpy as np
import part1 as p1

def divide_elementwise(numerators, denominators):
	'''Create an array by dividing each numerator
	by the corresponding denominator

	Numerators is a column vector
	Denominators is a row or column vector'''
	if denominators.ndim == 1:
		denominators = denominators[:, np.newaxis]

	return numerators.astype('float') / denominators.astype('float')

	
def divide_columns(array, denominators):
	'''Divide each column, elementwise, by a vector
	of denominators.'''
	result = np.empty((denominators.shape[0], 0))

	col_indices = range(array.shape[1])
	for c in col_indices:
		col = p1.select_cols(array, [c])
		result = np.hstack((result, 
			divide_elementwise(col, denominators)))

	return result


def run():
	a = np.arange(25).reshape(5, 5)
	b = np.array([1., 5, 10, 15, 20])
	# Start with missing array
	#result = np.empty(a.shape).fill(np.nan)
	print divide_columns(a, b)



