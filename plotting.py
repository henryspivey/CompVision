from PIL import Image
from pylab import *

# read image from array
try:
	im = array(Image.open("images/chives1.jpg"))
except IOError, e:
	raise e


#plot the image
imshow(im)

# some points
x = [100,100,400,400]
y = [200,500,200,500]

# plot with red stars
plot(x,y,'r*')
plot(x[:2], y[:2])


title("Plotting: chives1")

# axis('off')
show()

