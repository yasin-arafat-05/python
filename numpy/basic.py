import numpy as np



#------------------creatring fast np 1D array and print them and their type--------
arr = np.array([1,2,3,4])
print(arr)
print(type(arr))



#----------------------------check numpy version---------------------------
print("np version: "+np.__version__)


#-----------------------We can also create np arry with tuple---------------

arr1 = np.array((1,2,3,4,5))
print(arr1)
print(type(arr1))


#-------------------types of array and check Dimention----------------------
#--------------Check Array Element With Index Can be Negative -------------------------------

#0D array ----- Each value in an array is a 0-D array.
print("_____________0D array__________")
arr2 = np.array(23)
print(arr2)
print(arr2.ndim)


#1D arrray 
print("_____________1D array__________")
arr3 = np.array([1,2,3,4,5,6])
print(arr3)
print(f"access 3rd index element : {arr3[3]}")
print(f"access last index element : {arr3[-1]}")
print(arr3.ndim)


#2D array ()
print("_____________2D array__________")
arr4 = np.array([[1,2,3,4],[6,7,8,9]])
print(arr4)
print(type(arr4))
print(arr4.ndim)
print(f"Acces 2nd row 3 elemnet: {arr4[1,2]}")
print(f"Acces 2nd row 2 elemnet: {arr4[1,-3]}")

#3d array
#-------=-----LINK: https://www.youtube.com/watch?v=SjtXNJy9RCk --------------

print("_____________3D array__________")
arr5 = np.array([
                [[1, 2, 3],
                 [4, 5, 6]],

                [[7, 8, 9],
                [10, 111, 12]]]
                  )

# 2 x (2x3) (2D array)

print(arr5.ndim)
print(f"Access 3rd row 2 element: {arr5[1,1,1]}")

print("_____________Max 32D array__________")
#making 32 dimentional array (max dimention 32)
arr6 = np.array([1,2,3,4,5],ndmin=32)
print(arr6)
print(arr6.ndim)
