N, K, C = map(int, input().split())
items = list(map(int, input().split()))
items.sort()
prefix = [0] * (N + 1)
for i in range(1, N + 1):
    prefix[i] = prefix[i-1] + items[i-1]
max_range = N - K

if K >= N:
    ans = prefix[N]
    for _ in range(C):
        print(ans)
else:
    p = 0
    for x in range(1, C + 1):
        while p + 1 <= max_range and prefix[p + 1] <= x:
            p += 1
        print(prefix[p + K] - prefix[p])