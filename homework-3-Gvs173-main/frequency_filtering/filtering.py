# For this part of the assignment, You can use inbuilt functions to compute the fourier transform
# You are welcome to use fft that are available in numpy and opencv

import numpy as np


class Filtering:

    def __init__(self, image):
        """initializes the variables for frequency filtering on an input image
        takes as input:
        image: the input image
        """
        self.image = image
        self.mask = self.get_mask

    def get_mask(self, shape):
        """Computes a user-defined mask
        takes as input:
        shape: the shape of the mask to be generated
        rtype: a 2d numpy array with size of shape
        """
        fshift2 = np.copy(shape)
        fshift2[270:290, 210:230] = 0.001
        fshift2[222:238, 290:310] = 0.001
        fshift2[235:250, 230:245] = 0.001
        fshift2[265:280, 265:280] = 0.001
        mag_filtered_dft = 20 * np.log(np.abs(fshift2))
        print(mag_filtered_dft)
        return fshift2

    def post_process_image(self, image):
        """Post processing to display DFTs and IDFTs
        takes as input:
        image: the image obtained from the inverse fourier transform
        return an image with full contrast stretch
        -----------------------------------------------------
        You can perform post processing as needed. For example,
        1. You can perfrom log compression
        2. You can perfrom a full contrast stretch (fsimage)
        3. You can take negative (255 - fsimage)
        4. etc.
        """
        image = 255 * ((image - image.min()) / (image.max() - image.min()))
        return image

    def filter(self):
        """Performs frequency filtering on an input image
        returns a filtered image, magnitude of frequency_filtering, magnitude of filtered frequency_filtering
        ----------------------------------------------------------
        You are allowed to use inbuilt functions to compute fft
        There are packages available in numpy as well as in opencv
        Steps:
        1. Compute the fft of the image
        2. shift the fft to center the low frequencies
        3. get the mask (write your code in functions provided above) the functions can be called by self.filter(shape)
        4. filter the image frequency based on the mask (Convolution theorem)
        5. compute the inverse shift
        6. compute the inverse fourier transform
        7. compute the magnitude
        8. You will need to do post processing on the magnitude and depending on the algorithm (use post_process_image to write this code)
        Note: You do not have to do zero padding as discussed in class, the inbuilt functions takes care of that
        filtered image, magnitude of frequency_filtering, magnitude of filtered frequency_filtering: Make sure all images being returned have grey scale full contrast stretch and dtype=uint8
        """
        img = self.image
        f = np.fft.fft2(img)
        fshift = np.fft.fftshift(f)

        fshift2 = Filtering.get_mask(self, fshift)
        inv_fshift = np.fft.ifftshift(fshift2)
        img_recon = np.real(np.fft.ifft2(inv_fshift))
        img_recon2 = Filtering.post_process_image(self, img_recon)
        mag_dft = 20 * np.log(np.abs(fshift))
        mag_filtered_dft = 20 * np.log(np.abs(fshift2))
        return [img_recon2, mag_dft, mag_filtered_dft]
