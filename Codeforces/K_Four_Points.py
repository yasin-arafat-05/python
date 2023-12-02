import math
x1,y1 = map(int,input().split())
x2,y2 = map(int,input().split())
x3,y3 = map(int,input().split())

if x1==x2!=x3 and y1!=y2==y3:
    print(f"{x3} {y1}")
elif x1==x2!=x3 and y1==y2!=y3:
    print(f"{x3} {y3}")
elif x1==x2!=x3 and y1==y3!=y2:
    print(f"{x3} {y2}")
elif x1!=x2==x3 and y1==y3!=y2:
    print(f"{x1} {y2}")
elif x1!=x2==x3 and y1==y2!=y3:
    print(f"{x1} {y3}")
elif x1!=x2==x3 and y1!=y2==y3:
    print(f"{x1} {y1}")
elif x1==x3!=x2 and y1==y3!=y2:
    print(f"{x2} {y2}")
elif x1==x3!=x2 and y1==y2!=y3:
    print(f"{x2} {y3}")
elif x1==x3!=x2 and y1!=y2==y3:
    print(f"{x2} {y1}")
