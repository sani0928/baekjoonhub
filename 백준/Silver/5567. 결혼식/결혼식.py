import sys; from collections import deque
input = sys.stdin.readline
ans = 0
n, m = int(input()), int(input())
g = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)
q = deque([(1, 0)])
v = [0] * (n + 1)
v[1] = 1
while q:
    cur, dist = q.popleft()
    if dist == 2:
        continue
    for nx in g[cur]:
        if not v[nx]:
            v[nx] = 1
            ans += 1
            q.append((nx, dist + 1))
print(ans)