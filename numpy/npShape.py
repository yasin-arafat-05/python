import numpy as np

#For np:
arr = np.array([[1,2,3,4],[1,2,3,4]])
print(f"np array shape(each index contain element): {arr.shape} ")


arr1 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(f"np array shape(each index contain element): {arr1.shape} ")

#reshape the element:
arr2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr2.reshape(4, 3)
print(newarr)

print()
arr3 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
k = arr3.reshape(2, 3, 2)
print(k)
print()
