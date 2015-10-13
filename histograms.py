# Make an image histogram with the distribution of pixel values.

from PIL import Image
from pylab import *

# read image to array
im = array(Image.open("images/chives1.jpg").convert('L'))

# create a new figure
figure()
hist(im.flatten(),128) # image has to be flattened since hist() needs a 1 dimensional array as input.
					   # second argument defines the number of bins to use
show()
gray()

contour(im, origin="image")
axis('equal')
axis('off')


def histeq(im, nbr_bins=256):
	# im is grayscale image
	""" Histogram equalization of a grayscale image. """
	# get image histogram
	imhist, bins = histogram(im.flatten(). nbr_bins, normed=True)
	cdf = imhist.cumsum() # cdf function
	cdf = 255 * cdf/cdf[-1] # normalize

	im2 = interp(im.flatten(), bins[:-1], cdf)

	return im2.reshape(im.shape), cdf
