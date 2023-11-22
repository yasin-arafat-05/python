import numpy as np
#npCopy is the copy of the orginal array
arr = np.array([1,2,3,4,5])
copy = arr.copy()
arr[2] = 100
print(f"original: {arr}  Copy: {copy}")
print()

#npView is the view of the original array 
arr1 = np.array([6,7,8,9])
view = arr1.view()
print(f"original: {arr1}  View: {view}")
print("before changing original array.")
arr1[1]=1234
print(f"original: {arr1}  View: {view}")

#check it's copy or view:
print("Copy->(NONE) or View->(print the array): ")
print(copy.base)
print(view.base)