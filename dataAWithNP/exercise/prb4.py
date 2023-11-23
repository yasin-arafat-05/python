'''
Write a NumPy program to create a 3x3 array with random 
values and subtract the mean of each row from each element.
'''
import numpy as np 

arr = np.linspace(1,9,9,dtype=np.int64).reshape(3,3)
print(f"orginal array: \n {arr}")

mean = np.mean(arr,axis=1,keepdims=True,dtype=np.int64)
print(f"mean array : \n {mean}")

'''
python will broadcast the array (mean) into: 
[[2 2 2]
 [5 5 5]
 [8 8 8]]
'''
print(arr-mean)
