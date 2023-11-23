'''
Write a NumPy program to find the dot product of two arrays of different dimensions.

'''
import numpy as np
array1 = np.array([1,2,3,4,5,6,7,8,9]).reshape(3,3)
array2 = np.array([1,2,3]).reshape(3)

print(f"array1 : \n {array1}")
print()
print(f"array2 : \n {array2}")
print()

print(f"-----dot product:----- \n { np.dot(array1,array2)}")

