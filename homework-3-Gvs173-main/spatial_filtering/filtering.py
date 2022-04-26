import numpy as np


class Filtering:

    def __init__(self, image):
        self.image = image

    def get_gaussian_filter(self):
        """Initialzes/Computes and returns a 5X5 Gaussian filter"""
        gauss_filter = (1/273)* np.matrix([[1,4,7,4,1],[4,16,26,16,4],[7,26,41,26,7],[4,16,26,16,4],[1,4,7,4,1]])
        return gauss_filter

    def get_laplacian_filter(self):
        """Initialzes and returns a 3X3 Laplacian filter"""
        return np.matrix([[-1,0,-1],[0,4,0],[-1,0,-1]])

        #return np.zeros((3, 3))

    def filter(self, filter_name):
        """Perform filtering on the image using the specified filter, and returns a filtered image
            takes as input:
            filter_name: a string, specifying the type of filter to use ["gaussian", laplacian"]
            return type: a 2d numpy array
                """
        if filter_name=="gaussian":
            img=self.image
            f = Filtering.get_gaussian_filter(self)
            img1 = np.zeros([img.shape[0]+4,img.shape[1]+4])
            img1[2:img.shape[0]+2,2:img.shape[1]+2] = img
            new_variable = np.zeros(img.shape)
            for i in range(2, img.shape[0]+2):
                for j in range(2, img.shape[1]+2):
                    new_variable[i-2, j-2] = (np.multiply(img1[i-2:i+3, j-2:j+3], f)).sum()

        else:
            img=self.image
            f=Filtering.get_laplacian_filter(self)
            img1 = np.zeros([img.shape[0]+2,  img.shape[1]+2])
            img1[1:img.shape[0]+1, 1:img.shape[1]+1] = img
            new_variable = np.zeros(img.shape)
            for i in range(1, img.shape[0]+1):
                for j in range(1, img.shape[1]+1):
                    new_variable[i-1, j-1]= (np.multiply(img1[i-1:i+2, j-1: j+2], f)).sum()

        return new_variable

