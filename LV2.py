from cv2 import sqrt
import numpy as np
from scipy.ndimage.filters import gaussian_filter
import cv2

matrix = np.array([ [69, 124, 136, 220], 
                    [64, 112, 198, 200], 
                    [26, 89, 156, 21], 
                    [36, 78, 241, 180]
                  ])

matrixv4 = np.array([[-1, 0, 1], 
                    [-2, 0, 2], 
                    [-1, 0, 1]])

matrixv5 = np.array([[-1, -2, -1], 
                    [0, 0, 0], 
                    [1, 2, 1]])


#Logaritamska transformacija
for x in matrix:
  print(np.log(x+1))

matrixv2 = []
gamma = 0
#Gamma transformacija
for x in matrix:
    gamma = 1* x**0.7 #Mijenjaj po formuli
    print(gamma)
    matrixv2.append(gamma)

print("Lmax:",np.max(matrixv2))
print("Lmin:",np.min(matrixv2))
print("Lsr:",np.sum(matrixv2)/16)

