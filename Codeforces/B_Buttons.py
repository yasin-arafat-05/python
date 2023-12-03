n = int(input())

sum = n
j = 1
for _ in range(n):
    sum += (n-j)*j
    j +=1

print(sum)