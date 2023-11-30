import matplotlib
matplotlib.use('TkAgg')

# importing the required module 
import matplotlib.pyplot as plt 
	
# x axis values 
x = [1,2,3] 
# corresponding y axis values 
y = [2,4,1] 
plt.plot(x, y) 
plt.xlabel('x - axis') 
plt.ylabel('y - axis') 
plt.title('My first graph!') 
	
plt.show() 
