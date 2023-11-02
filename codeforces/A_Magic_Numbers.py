n = input()
i = 0

while i < len(n):
    if i + 2 < len(n) and n[i:i+3] == "144":
        i += 3
    elif i + 1 < len(n) and n[i:i+2] == "14":
        i += 2
    elif n[i] == "1":
        i += 1
    else:
        print("NO")
        break
else:
    print("YES")