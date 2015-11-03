import numpy as np
import matplotlib.pyplot as plt

class mandelbrotIterator(object):
    '''Uses some information from:
    http://kestrel.nmt.edu/~raymond/software/python_notes/paper003.html
    '''

    def __init__(self, xnum=20, ynum=20, y_bounds=(-1.5, 1.5), x_bounds=(-2, 1), n_max = 50):
        self.xnum = xnum
        self.ynum = ynum
        self.x_bounds = x_bounds
        self.y_bounds = y_bounds
        self.n_max = n_max
        self.make_grid()


    def make_grid(self):
        x = np.linspace(self.x_bounds[0], self.x_bounds[1], num=self.xnum)
        y = np.linspace(self.y_bounds[0], self.y_bounds[1], num=self.ynum)
        X, Y = np.meshgrid(x, y)
        self.grid = X + 1j*Y

    def iterate(self):
        z = self.grid
        for v in range(self.n_max):
            z = z**2 + self.grid
        return z

    def get_mandelbrot_set(self, threshold):
        print self.iterate()
        return np.abs(self.iterate()) < threshold

    def output_image(self, threshold, filename='mandelbrot.png'):
        mask = self.get_mandelbrot_set(threshold)
        print mask
        plt.imshow(mask.T, extent=[self.x_bounds[0], self.x_bounds[1], self.y_bounds[0], self.y_bounds[1]])
        plt.gray()
        plt.savefig(filename)




