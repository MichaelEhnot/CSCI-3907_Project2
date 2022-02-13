from skimage import io
from matplotlib import pyplot as plt
from scipy.ndimage import gaussian_filter
import numpy as np

# name of the input file
imname_low = 'basketball.jpg'
imname_high = 'orange.jpg'

# read in the image
im_low = io.imread(imname_low)
im_high = io.imread(imname_high)

# apply low pass filter to one image
s = 20
r_blur = gaussian_filter(im_low[:,:,0], sigma=s)
g_blur = gaussian_filter(im_low[:,:,1], sigma=s)
b_blur = gaussian_filter(im_low[:,:,2], sigma=s)
low_filtered = np.dstack([r_blur, g_blur, b_blur])

# apply high pass filter to other image
s = 7
r_blur = gaussian_filter(im_high[:,:,0], sigma=s)
g_blur = gaussian_filter(im_high[:,:,1], sigma=s)
b_blur = gaussian_filter(im_high[:,:,2], sigma=s)
high_filtered = np.dstack([r_blur, g_blur, b_blur])
high_filtered = im_high - high_filtered

# add the two images together
hybrid = low_filtered + high_filtered

# do a small gausian blur on hybrid image to remove artifacts from adding images together
s=4
r_blur = gaussian_filter(hybrid[:,:,0], sigma=s)
g_blur = gaussian_filter(hybrid[:,:,1], sigma=s)
b_blur = gaussian_filter(hybrid[:,:,2], sigma=s)
hybrid = np.dstack([r_blur, g_blur, b_blur])

io.imshow(low_filtered)
plt.show()
io.imshow(high_filtered)
plt.show()
io.imshow(hybrid)
plt.show()

#show log magnitude of forier transform for original images, filtered images, and hybrid images
plt.imshow(np.log(np.abs(np.fft.fftshift(np.fft.fft2(im_low)))))
plt.show()
plt.imshow(np.log(np.abs(np.fft.fftshift(np.fft.fft2(im_high)))))
plt.show()
plt.imshow(np.log(np.abs(np.fft.fftshift(np.fft.fft2(low_filtered)))))
plt.show()
plt.imshow(np.log(np.abs(np.fft.fftshift(np.fft.fft2(high_filtered)))))
plt.show()
plt.imshow(np.log(np.abs(np.fft.fftshift(np.fft.fft2(hybrid)))))
plt.show()

# save hybrid image
fname = 'hybrid_'+imname_low
io.imsave(fname, hybrid)

# notes: (15,5) for sample, (8,7) for quarter, (20,5) for fruit, (20,7) for basketball, (13,4) for pizza, (2) for final blur

