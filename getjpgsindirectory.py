import os


def get_imlist(path):
	"""Returns a list of filenames for all jpg images in a directory"""
	return [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.jpg')]




# ['./basilic1.jpg', './bg.jpg', './chives1.jpg', './coriander1.jpg', './herbes.jpg', './lemonbalm1.jpg', './rosemary1.jpg']