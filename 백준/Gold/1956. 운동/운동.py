import sys
input = sys.stdin.readline

INF = 10**9
ans = 10**9
n, m = map(int, input().split())
dist = [[INF] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b, w = map(int, input().split())
    dist[a][b] = w
for x in range(1, n + 1):
    for s in range(1, n + 1):
        for e in range(1, n + 1):
            if dist[s][x] == INF or dist[x][e] == INF: continue
            dist[s][e] = min(dist[s][e], dist[s][x] + dist[x][e])
for i in range(1, n + 1):
    ans = min(ans, dist[i][i])
print(ans if ans != 10**9 else -1)