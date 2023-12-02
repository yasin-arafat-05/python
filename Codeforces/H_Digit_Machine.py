l = list(map(int,input().split()))
index = 0
for i in range(len(l)):
    if l[i]==0:
        index = l[i]
ans = l[index]
ans = l[ans]
ans = l[ans]
print(ans)
