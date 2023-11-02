def big(a,b,c):
    if(a>b and a>c):
        return int(a)
    elif(b>a and b>c):
        return int(b)
    else:
        return int(c)

t = int(input())
for i in range(t):
    a,b,c,n= map(int,input().split())
    coin = [a,b,c]
    coin.sort()
    k = (2*coin[2])-coin[1]-coin[0]
    if((n>=k) and ((n-k)%3==0)):
      print("YES")
    else:
        print("NO")