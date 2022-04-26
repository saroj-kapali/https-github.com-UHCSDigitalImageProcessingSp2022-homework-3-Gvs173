# For this part of the assignment, please implement your own code for all computations,
# Do not use inbuilt functions like fft from either numpy, opencv or other libraries

import numpy as np
class Dft:
    def __init__(self):
        pass

    def forward_transform(self, matrix):
        """Computes the forward Fourier transform of the input matrix
        takes as input:
        matrix: a 2d matrix
        returns a complex matrix representing fourier transform"""
        output =  np.zeros([15,15],dtype="complex_")
        for x in range (15):
            for y in range(15):
                for i in range (15):
                    for j in range (15):
                        output[x,y] += matrix[i,j]*complex(np.cos(2*np.pi*x*i/15 + 2*np.pi*y*j/15),-np.sin(2*np.pi*x*i/15 + 2*np.pi*y*j/15))
        output= output/225
        return output

    def inverse_transform(self, matrix):
        """Computes the inverse Fourier transform of the input matrix
        You can implement the inverse transform formula with or without the normalizing factor.
        Both formulas are accepted.
        takes as input:
        matrix: a 2d matrix (DFT) usually complex
        returns a complex matrix representing the inverse fourier transform"""
        output =  np.zeros([15,15],dtype="complex_")
        for u in range (15):
            for v in range(15):
                for i in range (15):
                    for j in range (15):
                        output[u,v] += matrix[i,j]*complex(np.cos(2*np.pi*u*i/15 + 2*np.pi*v*j/15),+np.sin(2*np.pi*u*i/15 + 2*np.pi*v*j/15))
        return output


    def magnitude(self, matrix):
        """Computes the magnitude of the input matrix (iDFT)
        takes as input:
        matrix: a 2d matrix
        returns a matrix representing magnitude of the complex matrix"""
        output = np.zeros([15,15])
        for i in range (15):
            for j in range (15):
                output[i,j]= ((np.real(matrix[i,j]))**2 + (np.real(matrix[i,j]))**2)**(0.5)
        return output
