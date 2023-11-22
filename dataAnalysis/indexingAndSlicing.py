import numpy as np 
arr = np.array([11,12,13,14,13,14,15,19,15,16,17,21,63,92,36,18,98,32,81,23,17,18,19.5,43],ndmin=3).reshape(3,2,4)
print(f"\n array: {arr}")

#print a single elemnet
print(f"\n print a single element: {arr[1,1,2]}")

#print a 2d matrix 
print(f"\n print a 2d matrix: {arr[1]}")

#print a row 
print(f"\n print a row: {arr[1,1]}")

#print a subarray: 
print(f"Print a subarray using slicing : \n     {arr[1: , 0:1]}")

#print a subarray using ranges
print(f"\n subarray using ranges: \n{arr[1:, 0:1, :2]}")



