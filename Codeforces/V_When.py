n = int(input())
s = 21
m = 0
emm = n % 60
ans = ""

if n < 60:
    ans = f"{s}:{n:02d}"
else:
    h = n // 60
    for _ in range(h):
        s += 1
        if s == 24:
            s = 0
    ans = f"{s}:{emm:02d}"

print(ans)
