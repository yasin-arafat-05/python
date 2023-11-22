t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()
    res = a[0]
    s = 0

    for i in range(n):
        a[i] -= s
        s += a[i]

    for i in range(n):
        res = max(res, a[i])

    print(res)