
#
# Grab one of the original ffts files.

import matplotlib.pyplot as plt
from astropy.visualization import astropy_mpl_style
import numpy as np

from astropy.utils.data import get_pkg_data_filename
from astropy.io import fits


plt.style.use(astropy_mpl_style)

image_file = "/Users/andrewk/KEPLER/FFIs/kplr2009114174833_ffi-cal.fits"


fits.info(image_file)

image_data = fits.getdata(image_file, ext=1)
print(image_data)
print(image_data.shape)
plt.figure(num=None, figsize=(8, 6), dpi=300)
plt.imshow(image_data, cmap=plt.get_cmap('gray'), vmin=0, vmax=512)
plt.colorbar()
#plt.show()

plt.figure()


a = np.array(image_data)
flat = a.flatten()
#N_points = 100000
n_bins = 100

# Generate a normal distribution, center at x=0 and y=5
#x = np.random.randn(N_points)
#y = .4 * x + np.random.randn(100000) + 5

#fig, axs = plt.subplots(1, 2, sharey=True, tight_layout=True)

# We can set the number of bins with the `bins` kwarg
plt.hist(flat, bins=n_bins)
#axs[1].hist(y, bins=n_bins)

plt.show()
