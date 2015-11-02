
import unittest
import numpy as np
import seven.part1 as p1

class Part1TestCase(unittest.TestCase):
	'''Test the functions in the part1 module.'''

	def test_wrapped_array(self):
		array = p1.wrapped_array(1, 15, 3)
		test_array = array
		success = np.array(
			[[1,  6, 11],
			 [2,  7, 12],
			 [3,  8, 13],
			 [4,  9, 14],
			 [5, 10, 15]]
			)
		# Assert all elements of arrays are equal
		self.assertTrue((test_array==success).all())

	def test_select_rows(self):
		array = p1.wrapped_array(1, 15, 3)
		test_array = p1.select_rows(array, (1, 3))
		success = np.array([
				[2,  7, 12],
				[4,  9, 14]])
		# Assert all elements of arrays are equal
		self.assertTrue((test_array==success).all())

	def test_select_cols(self):
		array = p1.wrapped_array(1, 15, 3)
		test_array = p1.select_cols(array, (1))
		success = np.array([
				[6],
				[7],
				[8],
				[9],
				[10]
			])
		# Assert all elements of arrays are equal
		self.assertTrue((test_array==success).all())

	def test_select(self):
		array = p1.wrapped_array(1, 15, 3)
		test_array = p1.select(array, (1, 0), (3, 2))
		success = np.array([
				[2, 7, 12],
				[3,  8, 13],
			 	[4,  9, 14]
			])
		# Assert all elements of arrays are equal
		self.assertTrue((test_array==success).all())

	def test_filter(self):
		array = p1.wrapped_array(1, 15, 3)
		test_array = p1.filter(array, lambda x: 3 <= x <= 11)
		success = np.array([
				[np.nan,  6, 11],
				[np.nan,  7, np.nan],
			 	[3,  8, np.nan],
			 	[4,  9, np.nan],
			 	[5, 10, np.nan]
			])
		# Assert all elements of arrays are equal
		self.assertTrue((test_array==success).all())



