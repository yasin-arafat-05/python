t = int(input())

for _ in range(t):
    x, h, m = map(int, input().split())
    alarms = [list(map(int, input().split())) for _ in range(x)]
    alarms.sort()
    sleep_time = float('inf')  # Initialize sleep_time to positive infinity

    for k, p in alarms:
        if k > h or (k == h and p >= m):
            sleep_time = (k - h) * 60 + (p - m)
            break

    if sleep_time == float('inf'):
        sleep_time = (alarms[0][0] + 24 - h) * 60 + (alarms[0][1] - m)

    print(f"{sleep_time // 60} {sleep_time % 60}")
