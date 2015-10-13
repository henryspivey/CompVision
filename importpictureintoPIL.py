from PIL import Image # alwawys included
import os
from getjpgsindirectory import get_imlist
first = get_imlist("images")[1]
print get_imlist("images")
pil_im = Image.open(first) # creates a PIL image object

#pil_im=Image.open("herbes.jpg").convert("L") # converts from RGB to B & W

# Create thumbnails
pil_im.thumbnail((128,128)) # creates a thumbnail with the longest side 128px long

# Crop a region. .crop()
# The PIL library uses coordinate system (0,0) with (0,0) being in the upper left hand corner
box = (100,100,400,400)
region = pil_im.crop(box)

# Rotating an image
# pil_im=pil_im.rotate(45)

# Resizing an image
pil_im=pil_im.resize((230,230))
pil_im.show()
pil_im.save('pic1.jpg')

#takes all image files in a list of filenames and converts them to jpg
def convert(filelist):
	"""Convert images in a list to .jpg"""
	for infile in filelist:
		outfile  = os.path.splitext(infile)[0]+ '.jpg'
		if infile != outfile:
			try:
				Image.open(infile).save(outfile)
			except IOError:
				print "cannot convert", infile

def imresize(im,sz):
	""" Resize and image array using PIL """
	pil_im = Image.fromarray(uint8(im))
	return array(pil_im.resize(sz))

