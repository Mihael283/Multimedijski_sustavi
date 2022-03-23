from cv2 import sqrt
import numpy as np
from scipy.ndimage.filters import gaussian_filter
import cv2

matrix = np.array([ [93, 124, 31, 220], 
                    [64, 22, 129, 200], 
                    [142, 54, 156, 21], 
                    [36, 78, 241, 180]
                  ])

matrixv4 = np.array([[-1, 0, 1], 
                    [-2, 0, 2], 
                    [-1, 0, 1]])

matrixv5 = np.array([[-1, -2, -1], 
                    [0, 0, 0], 
                    [1, 2, 1]])

a =0
b= 0
c= 0
a = matrix[0][0] * matrixv4[0][0]
print(a)
b = matrix[0][0] * matrixv5[0][0]
print(b)


#Logaritamska transformacija
for x in matrix:
  print(np.log(x+1))

matrixv2 = []
gamma = 0
#Gamma transformacija
for x in matrix:
    gamma = 1* x**1.8 #Mijenjaj po formuli
    print(gamma)
    matrixv2.append(gamma)

print("Lmax:",np.max(matrixv2))
print("Lmin:",np.min(matrixv2))
print("Lsr:",np.sum(matrixv2)/16)

#Moving average
matrixv3 = []
avg = 0
for x in matrix:
    avg = x*1/9 #Mijenjaj po formuli
    print(avg)
    matrixv3.append(avg)

print("Lmax:",np.max(matrixv3))
print("Lmin:",np.min(matrixv3))
print("Lsr:",np.sum(matrixv3)/16)

print("GAUSD")
print(gaussian_filter(matrix,3))