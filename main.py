from skimage import io
from matplotlib import pyplot as plt
from scipy.ndimage import gaussian_filter

# name of the input file
imname_low = 'ski.PNG'
imname_high = 'bird.PNG'

# read in the image
im_low = io.imread(imname_low)
im_high = io.imread(imname_high)

# apply low pass filter to one image
low_filtered = gaussian_filter(im_low, sigma=10)

# apply high pass filter to other image
high_filtered = im_high - (gaussian_filter(im_high, sigma=5))

# add the two images together
hybrid = low_filtered + high_filtered

io.imshow(low_filtered)
plt.show()
io.imshow(high_filtered)
plt.show()
io.imshow(hybrid)
plt.show()

# notes: 15, 5 for sample