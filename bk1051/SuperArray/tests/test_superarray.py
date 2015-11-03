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
		success = np.arange(3, 12)
		# Assert all elements of arrays are equal
		self.assertTrue((test_array==success).all())

	def test_divide_elementwise(self):
		a = sa.SuperArray(np.arange(25).reshape(5, 5))
		a0 = a.select_cols([0])
		b = np.array([1., 5, 10, 15, 20])
		test_array = a._divide_column_elementwise(a0, b)
		success = np.array([[0], 
							[1], 
							[1],
							[1],
							[1]])
		print test_array
		print success
		self.assertTrue(
			(test_array==success).all()
			)

		a3 = a.select_cols([3])
		test_array = a._divide_column_elementwise(a3, b)
		success = np.array(
			[[3/1.], 
			[8/5.],
			[ 13/10.], 
			[18/15.], 
			[23/20.]])
		print test_array
		print success
		self.assertTrue(
			(test_array==success).all())

	def test_divide_columns(self):
		a = sa.SuperArray(np.arange(25).reshape(5, 5))
		b = np.array([1., 5, 10, 15, 20])

		a0 = a.select_cols([0])
		a1 = a.select_cols([1])
		a2 = a.select_cols([2])
		a3 = a.select_cols([3])
		a4 = a.select_cols([4])
		

		test_array = a.divide_columns(b)
		success = np.hstack([
			a._divide_column_elementwise(a0, b),
			a._divide_column_elementwise(a1, b),
			a._divide_column_elementwise(a2, b),
			a._divide_column_elementwise(a3, b),
			a._divide_column_elementwise(a4, b)	
			])


	def test_pick_col_closest_to(self):
		np.random.seed(12345)
		array = sa.SuperArray(np.random.rand(10, 3))
		success = np.array([
				[0.31637555],  
				[0.56772503],  
				[0.6531771],  
				[0.65356987],  
				[0.29870371],
         		[0.65641118],  
         		[0.64247533],  
         		[0.46759901],  
         		[0.43964461],  
         		[0.67687371]
			])
		test_array = array.pick_col_closest_to(0.5)
		diff = np.abs(test_array - success)
		print test_array
		self.assertTrue((diff < 0.00001).all())


	# Test factory methods
	def test_wrapped_array(self):
		test_array = sa.wrapped_array(1, 15, 3)
		success = sa.SuperArray(
			[[1,  6, 11],
			 [2,  7, 12],
			 [3,  8, 13],
			 [4,  9, 14],
			 [5, 10, 15]]
			)
		# Assert all elements of arrays are equal
		self.assertTrue((test_array==success).all())









