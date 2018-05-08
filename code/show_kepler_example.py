# Andrew Kaluzniacki
#
# Grab one of the original ffts files.

import matplotlib.pyplot as plt
from astropy.visualization import astropy_mpl_style
from astropy.io import fits

plt.style.use(astropy_mpl_style)

image_file = "/Users/andrewk/KEPLER/FFIs/kplr2009114174833_ffi-cal.fits"
fits.info(image_file)

image_data = fits.getdata(image_file, ext=1)
print(image_data)
print(image_data.shape)
plt.figure()
#plt.imshow(image_data, cmap='gray')
# The cmap change here is key to seeing the details.
plt.imshow(image_data, cmap=plt.get_cmap('gray'), vmin=0, vmax=1024)
plt.colorbar()
plt.show()