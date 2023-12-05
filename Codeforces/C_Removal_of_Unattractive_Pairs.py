def min_length_after_deletions(n, s):
    ans = 0
    for i in range(1, n):
        if s[i] == s[i - 1]:
            ans += 1

    return (ans + 1) // 2

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input().strip()
        result = min_length_after_deletions(n, s)
        print(result)

if __name__ == "__main__":
    main()
