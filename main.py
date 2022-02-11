from skimage import io
from matplotlib import pyplot as plt
from scipy.ndimage import gaussian_filter

# name of the input file
imname_low = 'bear.jpg'

# read in the image
im_low = io.imread(imname_low)

# apply low pass filter to one image
low_filtered = gaussian_filter(im_low, sigma=5)

io.imshow(low_filtered)
plt.show()