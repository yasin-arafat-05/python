t = int(input())

for _ in range(t):
    x, n, m = map(int, input().split())

    # Applying both Void Absorptions and Lightning Strikes in any order
    while n > 0 and x > 20:
        x = (x // 2) + 10
        n -= 1
    
    while m > 0:
        x -= 10
        m -= 1
    
    # Check if the dragon is defeated
    if x <= 0:
        print("YES")
    else:
        print("NO")
