
#
# Grab one of the original ffts files.

import matplotlib.pyplot as plt
from astropy.visualization import astropy_mpl_style
import numpy as np

from astropy.utils.data import get_pkg_data_filename
from astropy.io import fits


plt.style.use(astropy_mpl_style)

image_file = "/Users/andrewk/KEPLER/FFIs/kplr2009114174833_ffi-cal.fits"
image_file2 = "/Users/andrewk/KEPLER/FFIs/kplr2009114204835_ffi-cal.fits"


fits.info(image_file)

image_data = fits.getdata(image_file, ext=1)
print(image_data)
print(image_data.shape)
plt.figure(num=None, figsize=(8, 6), dpi=300)
plt.imshow(image_data, cmap=plt.get_cmap('gray'), vmin=0, vmax=512)
plt.colorbar()
plt.show()

fits.info(image_file2)

image_data2 = fits.getdata(image_file2, ext=1)
print(image_data2)
print(image_data2.shape)
plt.figure(num=None, figsize=(8, 6), dpi=300)
plt.imshow(image_data2, cmap=plt.get_cmap('gray'), vmin=0, vmax=512)
plt.colorbar()
plt.show()


plt.figure(num=None, figsize=(8, 6), dpi=300)
plt.imshow(image_data - image_data2,cmap=plt.get_cmap('gray'), vmin=-8, vmax=8)
plt.colorbar()
plt.show()