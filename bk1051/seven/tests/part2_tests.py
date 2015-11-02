import unittest
import numpy as np
import seven.part2 as p2
import seven.part1 as p1


class Part2TestCase(unittest.TestCase):
	'''Test the functions in the part2 module.'''

	def test_divide_elementwise(self):
		a = np.arange(25).reshape(5, 5)
		a0 = p1.select_cols(a, [0])
		b = np.array([1., 5, 10, 15, 20])
		test_array = p2.divide_elementwise(a0, b)
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

		a3 = p1.select_cols(a, [3])
		test_array = p2.divide_elementwise(a3, b)
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
		a = np.arange(25).reshape(5, 5)
		b = np.array([1., 5, 10, 15, 20])

		a0 = p1.select_cols(a, [0])
		a1 = p1.select_cols(a, [1])
		a2 = p1.select_cols(a, [2])
		a3 = p1.select_cols(a, [3])
		a4 = p1.select_cols(a, [4])
		

		test_array = p2.divide_columns(a, b)
		success = np.hstack([
			p2.divide_elementwise(a0, b),
			p2.divide_elementwise(a1, b),
			p2.divide_elementwise(a2, b),
			p2.divide_elementwise(a3, b),
			p2.divide_elementwise(a4, b)	
			])
