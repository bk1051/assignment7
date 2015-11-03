'''
Program: assignment7.py
Author: Brian Karfunkel

This program outputs stuff.

'''

import SuperArray as sa
import numpy as np
import seven.mandelbrotIterator as mi


'''Question 1'''
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




'''Question 2'''
a = sa.SuperArray(np.arange(25).reshape(5, 5))
b = sa.SuperArray([1., 5, 10, 15, 20])
print "\n\nQuestion 2:\n"
print a.divide_columns(b)


'''Question 3'''



'''Question 4'''
foo = mi.mandelbrotIterator()
foo.output_image(2)
foo.output_image(1, 'mandelbrot1.png')
foo.output_image(3, 'mandelbrot3.png')

bar = mi.mandelbrotIterator(n_max=10)
bar.output_image(2, 'mandelbrot_bar.png')



