k = int(input())
l = map(int,input().split())
month = []
for i in l:
    month.append(i)
month.sort(reverse=True)

if k==0:
    print(0)
else:
    ans = 0
    finalAns = 0 
    for i in month:
        if(ans<k):
            ans +=i
            finalAns+=1
    print(finalAns)
