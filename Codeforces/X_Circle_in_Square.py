import math
t = int(input())
for i in range(t):
    r = float(input())
    ans =float(((r*2)**2) - (math.pi*r*r))
    print(f"Case {i+1}: {round(ans,2)}")
