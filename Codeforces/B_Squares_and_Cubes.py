import math

def count_squares_and_cubes(n):
    ans  = set()
    max_val = int(math.sqrt(n)) + 2

    # Count squares
    for i in range(1, max_val):
        if i * i <= n:
            ans.add(i*i)

    # Count cubes
    for i in range(1, int(n**(1/3)) + 2):
        if i * i * i <= n:
            ans.add(i*i*i)
    return len(ans)


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        result = count_squares_and_cubes(n)
        print(result)

if __name__ == "__main__":
    main()
