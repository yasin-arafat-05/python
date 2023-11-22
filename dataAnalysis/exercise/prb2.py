'''
Write a NumPy program to create a 3x3 identity matrix and stack it vertically and horizontally.

'''
import numpy as np 
matrix = np.eye(3,dtype=int)
print(f"Identity matrix: \n {matrix}")
print()

#stack the matrix vertically
vertically_stack = np.concatenate((matrix,matrix),axis=0)
print(f"Stack Matrix Vertically: \n {vertically_stack}")
print()
#stack the matrix horizontally 
print(f"Stack Matrix Horizontally : \n {np.concatenate((matrix,matrix),axis=1)}")
