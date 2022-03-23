
import numpy as np
  
matrix = np.array([ [110, 124, 220, 123], 
                    [64, 81, 154, 200], 
                    [21, 50, 126, 162], 
                    [123, 78, 131, 180]
                  ])
  
#Mean
sd = np.mean(matrix)
print("Mean :\n", sd)
#Standard deviation
sd = np.std(matrix)
print("Standard Deviation :\n", sd)