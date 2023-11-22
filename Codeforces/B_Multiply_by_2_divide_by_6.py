t = int(input())

for _ in range(t):
    n = int(input())
    moves = 0

    while n > 1:
        if n % 6 == 0:
            n //= 6
        elif n % 3 == 0:
            n *= 2
        else:
            moves = -1
            break

        moves += 1

    print(moves)
