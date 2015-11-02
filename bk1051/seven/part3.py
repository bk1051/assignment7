import numpy as np
import part1 as p1

def generate_array():


def run():
	# Create a random 10x3 array
	# To test closeness to 0.5, we subtract 0.5 from each element
	array = np.random.rand(10, 3) - 0.5
	array_abs = np.abs(array)
	argsorted = array_abs.argsort(axis=1)
	min_col = p1.select_cols(argsorted, [0])

	print array[np.arange(10), min_col.T]





