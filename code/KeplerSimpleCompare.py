#
# Display 8 full frame images - one can 'blink' between them and see
# some obvious differences.

import matplotlib.pyplot as plt
from astropy.visualization import astropy_mpl_style
import numpy as np

from astropy.utils.data import get_pkg_data_filename
from astropy.io import fits


plt.style.use(astropy_mpl_style)

fileList = [
            "kplr2009114174833_ffi-cal.fits",
            "kplr2009114204835_ffi-cal.fits",
            "kplr2009115002613_ffi-cal.fits",
            "kplr2009115053616_ffi-cal.fits",
            "kplr2009115080620_ffi-cal.fits",
            "kplr2009115131122_ffi-cal.fits",
            "kplr2009115173611_ffi-cal.fits",
            "kplr2009116035924_ffi-cal.fits"
            ]


for file in fileList:
    file = "/Users/andrewk/KEPLER/FFIs/" + file
    #fits.info(file)
    image_data = fits.getdata(file, ext=1)
    print(image_data[0])
    print(image_data.shape)
    plt.figure(num=None)
    plt.imshow(image_data, cmap=plt.get_cmap('gray'), vmin=0, vmax=512)
    plt.colorbar()
    plt.show()

# fits.info(image_file2)
#
# image_data2 = fits.getdata(image_file2, ext=1)
# print(image_data2)
# print(image_data2.shape)
# plt.figure(num=None, figsize=(8, 6), dpi=300)
# plt.imshow(image_data2, cmap=plt.get_cmap('gray'), vmin=0, vmax=256)
# plt.colorbar()
# plt.show()
#
#
# plt.figure(num=None, figsize=(8, 6), dpi=300)
# plt.imshow(image_data - image_data2,cmap=plt.get_cmap('gray'), vmin=-8, vmax=8)
# plt.colorbar()
# plt.show()