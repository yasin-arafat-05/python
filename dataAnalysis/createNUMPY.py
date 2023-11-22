import numpy as np

print("__________________x______________________")
#filed with zero
print(f"np.zeros(2,2,4)  \n {np.zeros((3,2,4))}")

print("__________________x______________________")
#filled with one
print(f"np.ones(2,2,4)  \n {np.ones((3,2,4))}")

print("__________________X______________________")

#identity matrix
print(f"np.eye(2,2,4)  \n {np.eye((4))}")
print("__________________X______________________")

#create random vector:
print(f"np.random.random(3) \n {np.random.random(3)}")
print("__________________X______________________")

#create random vector between a range(for 2D -> greater than or equal to 2)
print(f"np.random.randn(3) \n {np.random.randn(2,3)}")
print("__________________X______________________")

#create a fixed array with fixed value:(2D)
print(f"np.full([2,3],42) \n {np.full([2,3],42)}")

print("__________________X______________________")
#range with start and end value 
print(f"np.arrange(10,90) \n {np.arange(10,110,10)}")
print()
print(f"np.arrange(10,90) \n {np.arange(10,90,3).reshape(3,3,3)}")

print("__________________X______________________")
#Equally space number:  range , the number i want 

print(f"np.linspace(3,90,6) \n {np.linspace(3,90,6)}")
