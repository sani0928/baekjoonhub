import sys
input = sys.stdin.readline

n, k = map(int, input().split())
d = [[float('inf')] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    d[i][i] = 0

for _ in range(k):
    u, v = map(int, input().split())
    d[u][v] = 1

for m in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            d[i][j] = min(d[i][j], d[i][m] + d[m][j])

for _ in range(int(input())):
    a, b = map(int, input().split())
    if d[a][b] == d[b][a]:
        print(0)
        continue
    if d[a][b] < d[b][a]:
        print(-1)
    else:
        print(1)