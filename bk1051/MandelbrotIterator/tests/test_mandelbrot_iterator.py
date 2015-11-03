import unittest
import numpy as np
import MandelbrotIterator as mi

class MandelbrotIteratorTestCase(unittest.TestCase):
	'''Test case to test the MandelbrotIterator class'''

	def test_creates_grid_on_init(self):
		iterator = mi.MandelbrotIterator()
		self.assertIsNotNone(iterator.grid)

	def test_grid(self):
		iterator = mi.MandelbrotIterator(xnum=3, ynum=3)
		test_array = iterator.grid
		success = np.array([[-2.0-1.5j, -0.5-1.5j,  1.0-1.5j],
	       [-2.0+0.j , -0.5+0.j ,  1.0+0.j ],
	       [-2.0+1.5j, -0.5+1.5j,  1.0+1.5j]])
		# Assert all elements of arrays are equal
		self.assertTrue((test_array==success).all())

	def test_iterate(self):
		iterator = mi.MandelbrotIterator(xnum=3, ynum=3, n_max=2)
		test_array = iterator.iterate(2)
		success = np.array([[-22.1875-3.75j,   5.7500-1.5j , -19.1875+0.75j],
					       [  2.0000+0.j  ,  -0.4375+0.j  ,   5.0000+0.j  ],
					       [-22.1875+3.75j,   5.7500+1.5j , -19.1875-0.75j]])
		
		# Assert all elements of arrays are equal
		self.assertTrue((test_array==success).all())

