from math import ceil
n, m = int(input()), int(input())
lamps = list(map(int, input().split()))
mx = max(lamps[0], n - lamps[m - 1])
for i in range(1, m):
    mx = max(mx, ceil((lamps[i] - lamps[i - 1]) / 2))
print(mx)