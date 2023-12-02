import math

n = int(input())
x = math.sqrt(n * (12800000 + n))
ans = "{:.9f}".format(x)

print(ans)
