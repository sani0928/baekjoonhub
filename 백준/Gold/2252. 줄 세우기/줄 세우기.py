import sys
from collections import deque
input = sys.stdin.readline

N, M  = map(int, input().split())
graph = [[] for _ in range(N + 1)]
in_degree = [0] * (N + 1)
ans = []
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    in_degree[v] += 1

q = deque()
for i in range(1, N + 1):
    if in_degree[i] == 0:
        q.append(i)

while q:

    cur = q.popleft()
    ans.append(cur)

    for nx in graph[cur]:
        in_degree[nx] -= 1
        if in_degree[nx] == 0:
            q.append(nx)

print(*ans)