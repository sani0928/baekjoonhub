import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    lst = []
    q = deque([s])
    while q:
        cur = q.popleft()
        lst.append(cur)
        for nx in tree[cur]:
            if nx == parent[cur]:
                continue
            if parent[nx] != 0:
                continue
            parent[nx] = cur
            q.append(nx)
    return lst

n, s, d = map(int, input().split())
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

parent = [0] * (n + 1)
parent[s] = 0
order = bfs()
height = [-1] * (n + 1)
for u in reversed(order):
    mx_h = -1
    for v in tree[u]:
        if v == parent[u]:
            continue
        if height[v] > mx_h:
            mx_h = height[v]
    if mx_h == -1:
        height[u] = 0
        continue
    height[u] = mx_h + 1

foot = 0
for node in range(1, n + 1):
    if parent[node] == 0:
        continue
    if height[node] >= d:
        foot += 1
print(2 * foot)