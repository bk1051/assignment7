import numpy as np
import matplotlib.pyplot as plt

class MandelbrotIterator(object):
    '''A class to describe a grid of complex numbers, which
    is then iterated to create a Mandelbrot Set. That set
    can also be output as an image.

    Uses some information on complex numbers in Python from:
    http://kestrel.nmt.edu/~raymond/software/python_notes/paper003.html
    '''

    def __init__(self, xnum=50, ynum=50, x_bounds=(-2, 1), y_bounds=(-1.5, 1.5), n_max = 50):
        '''Constructor. Set up the grid and initialize the MandelbrotIterator.

        Args:
            xnum: the number of points on the x axis of the grid
            ynum: the number of points on the y axis of the grid
            x_bounds: a tuple of the bounds of the x axis of the grid
            y_bounds: a tuple of the bounds of the y axis of the grid
            n_max: the maximum number of iterations
        '''
        self.xnum = xnum
        self.ynum = ynum
        self.x_bounds = x_bounds
        self.y_bounds = y_bounds
        self.n_max = n_max
        self.make_grid()


    def make_grid(self):
        '''Initialize the grid.'''
        x = np.linspace(self.x_bounds[0], self.x_bounds[1], num=self.xnum)
        y = np.linspace(self.y_bounds[0], self.y_bounds[1], num=self.ynum)
        X, Y = np.meshgrid(x, y)
        self.grid = X + 1j*Y

    def iterate(self, n_max=None):
        '''Run the iteration on the grid.

        Args:
            n_max (optional): the number of iterations. Defaults to self.n_max
        Returns:
            An array resulting from iterating the grid of complex numbers.

        Note that the calculation may raise a RuntimeWarning, as the calculations
        can overflow the floating point arithmetic. The default
        behavior of Numpy is correct, though, so we can ignore it.
        '''
        # Ignore floating point errors
        np.seterr(over='ignore', invalid='ignore')
        if not n_max:
            n_max = self.n_max

        z = self.grid

        for v in range(n_max):
            z = z**2 + self.grid
        return z

    def mandelbrot_set(self, threshold=50):
        '''Return the Mandelbrot set.

        The Mandelbrot set is the set of points in the iterated grid
        for which the absolute value is less than some threshold. The
        set is respresented as a boolean mask array, where the points
        are True if they are in the set and False otherwise.
        '''
        return np.abs(self.iterate()) < threshold

    def output_image(self, threshold=50, filename='mandelbrot.png'):
        '''Output an image of the Mandelbrot set.

        Args:
            threshold: The threshold for determining the Mandelbrot set
            filename: the output file for the image that is produced
        '''
        mask = self.mandelbrot_set(threshold)
        plt.imshow(mask.T, extent=[self.x_bounds[0], self.x_bounds[1], self.y_bounds[0], self.y_bounds[1]])
        plt.gray()
        plt.savefig(filename)




