t = int(input())
for _ in range(t):
    a,b = map(int,input().split())
    if b==1:
        print("NO")
    else:
        print("YES")
        z = a*b
        x = a 
        y = a * (b-1)
        if x==y:
            print(f"{x} {2*z-x} {2*z}")
        else:
            print(f"{x} {y} {z}")
