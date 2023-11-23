import numpy as np 

arr2 = np.array([1,1,1,1,1,1,1,1,1,1,1,1],ndmin=2).reshape(3,4)
arr3 = np.array([11,12,13,14,15,16,17,18,19,11,12,13],ndmin=2).reshape(3,4)


#Add two array
print(arr2+arr3)
print()

#Add a scalar
print(arr2+3)
print()

#division by scalar 
print(arr2/2)
print()

#multiplication by scalar 
print(arr2*0)
print()

#modulus with scalar 
print(arr3%2)
print()

# ___________________ Array Broadcasting _____________________
# Numpy arrays also support broadcasting, allowing arithmetic operations between two arrays 
# with different numbers of dimensions but compatible shapes. 
# Let's look at an example to see how it works.
print(f"Array 2: {arr2}")
print(f"shape of array 2 ---> {np.shape(arr2)}")
arr4 = np.array([4,5,6,7])
print(f"shape of array 2 ---> {np.shape(arr4)}")

# first numpy will reshape the array into (3,4) the perform the 
# if we not have arr4 = [1,2] we can't do addition.
print(f"Addition of arr2 and arr4: {arr2+arr4}")
