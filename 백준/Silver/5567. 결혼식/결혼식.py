import sys
input = sys.stdin.readline
ans = 0
n, m = int(input()), int(input())
g = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)
s = [1]
d = [0] * (n + 1)
d[1] = 1
while s:
    cur = s.pop()
    if d[cur] == 3:
        continue
    for nx in g[cur]:
        if not d[nx]:
            d[nx] = d[cur] + 1
            ans += 1
            s.append(nx)
print(ans)