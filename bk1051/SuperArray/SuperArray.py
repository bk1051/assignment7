import numpy as np

class SuperArray(np.ndarray):
	'''SuperArray is a utility class that adds
	extra functionality to np.array'''

	def __new__(cls, array):
		'''SuperArray is a subclass of ndarray,
		but we want the interface to be like np.array.
		So, to create a SuperArray, we pass it an array
		object, which is returned as a SuperArray.'''
		return np.asarray(array).view(cls)


	def select_rows(self, rows):
		'''Returns specified rows of the array.

		rows is an iterable
		'''
		return self[rows, :]
	

	def select_cols(self, cols):
		'''Returns specified columns of an array.

		cols is an iterable		
		'''
		return self[:, cols]


	def select(self, start, end):
		'''Returns a rectangular portion of an array.

		start is a tuple/list with the coordinates for the
			upper left of the rectangular portion
		end is a tuple/list with the coordinates for the
			lower right of the rectangular portion
		'''
		return self[start[0]:end[0]+1, start[1]:end[1]+1]


	def filter_array(self, function):
		'''Returns an array where each value is filtered.

		For each value in the array, the value is passed
		to function. If the result is True, the value is 
		included in the final array. If it is false, it is
		replaced with missing (None)
		'''
		# Create an array of same shape as array, but all missing
		result = np.empty(self.shape, dtype='bool')
		missing = np.empty(self.shape).fill(np.nan)

		for r, row in enumerate(self):
			for c, value in enumerate(row):
				result[r, c] = function(value)

		# np.where replaces the np.nan values in missing with None
		return np.where(result, self, missing)