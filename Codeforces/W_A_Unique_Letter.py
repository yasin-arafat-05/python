str = input()
a = str[0]
b = str[1]
c = str[2]

if a==b==c:
    print(-1)
elif a==b!=c:
    print(c)
elif a!=b==c:
    print(a)
elif a==c!=b:
    print(b)
elif a!=b!=c:
    print(a)