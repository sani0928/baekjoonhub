import sys; from collections import deque
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
for i in range(1, n + 1):
    graph[i].sort()
order = 1
q = deque([r])
vis = [0] * (n + 1)
vis[r] = 1
while q:
    cur = q.popleft()
    for nx in graph[cur]:
        if vis[nx]:
            continue
        order += 1
        vis[nx] = order
        q.append(nx)
print(*(vis[i] for i in range(1, n + 1)), sep='\n')