#By default python have
#string, integer, float , boolean and complex data type
import numpy as np 
arr = np.array([1,2,3,4,5])
print(f"Data type of arr: {arr.dtype}")


#"U7" means Unicode strings with a maximum length of 7 characters.
arr1 = np.array(['yasin','arafat','hossain'])
print(f"data type of arr1 is: {arr1.dtype}")



#creating array with a define data type
# "|S1" represents a NumPy data type for one-character strings
arr2 = np.array([1,2,3,4,4],dtype='S') 
print(f"data type of arr2: {arr2.dtype}")

arr3 = np.array([5,6,7,8],dtype="f") # convert into float or 
arr4 = arr3.astype('f')
arr5 = np.float64(arr3)

print(f"data type: {arr3.dtype} and it's value is: {arr3}")
print(f"data type: {arr4.dtype} and it's value is: {arr4}")
print(f"data type: {arr5.dtype} and it's value is: {arr5}")
print()
