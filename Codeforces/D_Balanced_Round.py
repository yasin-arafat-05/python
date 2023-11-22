t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    arr.sort()
    ans = mx = cons = 0
    for i in range(n):
        cons +=1
        if(i==n-1 or (arr[i+1] - arr[i])>k ):
            mx = max(mx,cons)
            cons = 0 
    ans = n - mx 
    print(ans)