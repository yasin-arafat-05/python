import numpy as np
a,b=map(int,input().split())
c,d=map(int,input().split())
e,f=map(int,input().split())

arr = np.array([c,d,e,f],ndmin=2).reshape(2,2)
print(arr[a-1][b-1])
