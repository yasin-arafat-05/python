a,b = map(int,input().split())
big = smll = 0

if(a>b):
    big = a
    smll = b
elif b>a:
    big = b 
    smll = a

if((11-big)==smll):
    print("Yes")
elif a==(b+1) or b==(a+1):
    print("Yes")
else:
    print("No")
