import sys
from collections import deque
input = sys.stdin.readline

n, m = int(input()), int(input())
road = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
    info = [0] + list(map(int, input().split()))
    for j in range(1, n + 1):
        if info[j] == 1:
            road[i].append(j)
schedule = tuple(map(int, input().split()))
vis = [0] * (n + 1)
vis[schedule[0]] = 1
q = deque([schedule[0]])
while q:
    cur = q.popleft()
    for nx in road[cur]:
        if vis[nx]:
            continue
        vis[nx] = 1
        q.append(nx)
ans = 0
for city in schedule:
    if vis[city] == 1:
        ans += 1
print('YES' if ans == m else 'NO')