from PIL import Image
from pylab import *

im = array(Image.open('images/chives1.jpg'))
imshow(im)

print "Please click 3 points"
x = ginput(3)

print "You clicked: ", x
show()
