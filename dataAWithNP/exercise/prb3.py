'''
Write a NumPy program to create a 4x4 array with random values and find the sum of each row.

'''

import numpy as np

mat = np.linspace(1,16,16,dtype=np.int64).reshape(4,4)
sum = np.sum(mat,axis=1)

print(f"matrix : \n {mat}")
print()
print(sum)
