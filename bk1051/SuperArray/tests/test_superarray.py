import unittest
import numpy as np
import SuperArray as sa

class SuperArrayTestCase(unittest.TestCase):
	'''Test the SuperArray class'''

	def test_create_superarray(self):
		array = sa.SuperArray([1,2,3])
		test_array = array
		success = np.array([1,2,3])
		self.assertTrue((test_array==success).all())

	def test_select_rows(self):
		array = sa.SuperArray(
			[[1,  6, 11],
			 [2,  7, 12],
			 [3,  8, 13],
			 [4,  9, 14],
			 [5, 10, 15]]
			)
		test_array = array.select_rows((1, 3))
		success = np.array([
				[2,  7, 12],
				[4,  9, 14]])
		# Assert all elements of arrays are equal
		self.assertTrue((test_array==success).all())

	def test_select_cols(self):
		array = sa.SuperArray(
			[[1,  6, 11],
			 [2,  7, 12],
			 [3,  8, 13],
			 [4,  9, 14],
			 [5, 10, 15]]
			)
		test_array = array.select_cols([1])
		print test_array
		success = np.array([
				[6],
				[7],
				[8],
				[9],
				[10]
			])
		print success
		# Assert all elements of arrays are equal
		self.assertTrue((test_array==success).all())

	def test_select(self):
		array = sa.SuperArray(
			[[1,  6, 11],
			 [2,  7, 12],
			 [3,  8, 13],
			 [4,  9, 14],
			 [5, 10, 15]]
			)
		test_array = array.select((1, 0), (3, 2))
		print test_array
		success = np.array([
				[2, 7, 12],
				[3,  8, 13],
			 	[4,  9, 14]
			])
		print success
		# Assert all elements of arrays are equal
		self.assertTrue((test_array==success).all())

	def test_filter_array(self):
		array = sa.SuperArray(
			[[1,  6, 11],
			 [2,  7, 12],
			 [3,  8, 13],
			 [4,  9, 14],
			 [5, 10, 15]]
			)
		test_array = array.filter_array(lambda x: 3 <= x <= 11)
		success = np.array([
				[None,  6, 11],
				[None,  7, None],
			 	[3,  8, None],
			 	[4,  9, None],
			 	[5, 10, None]
			])
		# Assert all elements of arrays are equal
		self.assertTrue((test_array==success).all())