'''
Program: assignment7.py
Author: Brian Karfunkel

This program uses the SuperArray class to manipulate
arrays and output the results. It then uses a
mandelbrotIterator to create an image of a Mandelbrot
set.
'''

try:
	import SuperArray as sa
	import numpy as np
	import MandelbrotIterator as mi

	def question_1():
		'''Outputs responses to Question 1'''
		array = sa.wrapped_array(1, 15, 3)
		print "\n\nInitial Array:\n", array

		def question_1a(superarray):
			print superarray.select_rows((1, 3))

		def question_1b(superarray):
			print superarray.select_cols([1])

		def question_1c(superarray):
			print superarray.select((1, 0), (3, 2))

		def question_1d(superarray):
			print superarray.filter_array(lambda x: 3 <= x <= 11)

		print "\n\nQuestion 1a:\n"
		question_1a(array)

		print "\n\nQuestion 1b:\n"
		question_1b(array)

		print "\n\nQuestion 1c:\n"
		question_1c(array)

		print "\n\nQuestion 1d:\n"
		question_1d(array)


	def question_2():
		'''Outputs the answer to Question 2'''
		a = sa.SuperArray(np.arange(25).reshape(5, 5))
		b = sa.SuperArray([1., 5, 10, 15, 20])
		print "\n\nQuestion 2:\n"
		print a.divide_columns(b)

	def question_3():
		'''Outputs the answer to Question 3'''
		# Create random 10x3 array
		superarray = sa.SuperArray(np.random.rand(10, 3))
		# Extract the element in each row closest to 0.5
		closest_els = superarray.pick_col_closest_to(0.5)

		print "\n\nQuestion 3:\n"
		print closest_els

	def question_4():
		'''Outputs the answer to Question 4'''
		print "\n\nQuestion 4:\n"
		mandelbrot = mi.MandelbrotIterator()
		mandelbrot.output_image()
		print "Mandelbrot set image saved"
		print mandelbrot.mandelbrot_set()


	if __name__ == '__main__':
		question_1()
		question_2()
		question_3()
		question_4()

except KeyboardInterrupt:
	print "Program ended because of user input"
