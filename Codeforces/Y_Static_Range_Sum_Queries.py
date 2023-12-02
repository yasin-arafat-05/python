import numpy as np
a,b = map(int,input().split())
l = list(map(int,input().split()))

nparray = np.array(l)

for _ in range(b):
    h,l = map(int,input().split())
    sum = nparray[(h-1):l].sum()
    print(sum)
    