t = int(input())
for _ in range(t):
    n = int(input())
    strn = input()
    pre = [0] * n
    suff = [0] * n
    s = set()
    
    for i in range(n):
        s.add(strn[i])
        pre[i] = len(s)
    
    s.clear()

    for i in range(n - 1, -1, -1):
        s.add(strn[i])
        suff[i] = len(s)
    
    ans = 0
    for i in range(n - 1):
        ans = max(ans, pre[i] + suff[i + 1])
    print(ans)
