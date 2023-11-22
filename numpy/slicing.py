import numpy as np
# for 1D npArray same as list

# 2D np Array

arr = np.array([[1,2,3,4],
               [5,6,7,8]])

print("--------2D Numpy Array: ---------")
print(arr[1,0:2])
print(arr[0,-3:-1])

print("-------Stepping : --------")
print(arr[1,0::2])