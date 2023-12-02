k = int(input())
ans = 1
for _ in range(k):
    ans = (ans%(1e9 + 7) * 2%(1e9+7))%(1e9+7)
print(int(ans))