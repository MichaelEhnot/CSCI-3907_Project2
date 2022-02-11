from skimage import io
from matplotlib import pyplot as plt

# name of the input file
imname = 'bear.jpg'

# read in the image
im = io.imread(imname)

io.imshow(im)
plt.show()