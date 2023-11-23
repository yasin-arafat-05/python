'''
Write a NumPy program to create a 3x3 array with random values and 
subtract the mean of each column from each element.
'''
import numpy as np

arr = np.linspace(1,9,9).reshape(3,3)
print(f"original array : \n {arr}")
mean = np.mean(arr,axis=0)
print(f"mean array : \n {mean}")

print("subtraction: ")
print(arr-mean)
