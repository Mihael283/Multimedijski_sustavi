# import the necessary packages
from __future__ import print_function
import numpy as np
import argparse
import cv2

matrix = np.array([ [93, 124, 31, 220], 
                    [64, 22, 129, 200], 
                    [142, 54, 156, 21], 
                    [36, 78, 241, 180]
                  ])


#matrix = matrix.astype("uint8")

"""
def adjust_gamma(image, gamma):

	# build a lookup table mapping the pixel values [0, 255] to
	# their adjusted gamma values
	table = np.array([((i / 255.0) ** gamma) * 255
		for i in np.arange(0, 256)]).astype("uint8")
	# apply gamma correction using the lookup table
	return cv2.LUT(image, table)

adjusted = adjust_gamma(matrix, 1.8)
print(adjusted)
print("Lmax:",np.max(adjusted))
print("Lmin:",np.min(adjusted))
print("Lsr:",np.sum(adjusted)/16)  
"""

def blur(a):
    kernel = np.array([[1/9,1/9,1/9], [1/9,1/9,1/9], [1/9,1/9,1/9]])
    kernel = kernel / np.sum(kernel)
    arraylist = []
    for y in range(3):
        temparray = np.copy(a)
        temparray = np.roll(temparray, y - 1, axis=0)
        for x in range(3):
            temparray_X = np.copy(temparray)
            temparray_X = np.roll(temparray_X, x - 1, axis=1)*kernel[y,x]
            arraylist.append(temparray_X)

    arraylist = np.array(arraylist)
    arraylist_sum = np.sum(arraylist, axis=0)
    return arraylist_sum

avg=blur(matrix)
print(avg)
print("Lmax:",np.max(avg))
print("Lmin:",np.min(avg))
print("Lsr:",np.sum(avg)/16)  

"""
def gaussian(sigma,Y,X):
    kernel = np.zeros((Y,X))
    ax = range(X) - np.floor(X/2)
    ay = range(Y) - np.floor(Y/2)
    xx,yy = np.meshgrid(ax,ay)
    kernel = np.exp(-0.5 * (np.square(xx) + np.square(yy)))/np.square(sigma)
    kernel = kernel/np.sum(kernel)
    return kernel 
"""
