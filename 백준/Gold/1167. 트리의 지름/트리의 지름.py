import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n + 1)]
for _ in range(n):
    info = list(map(int, input().split()))
    u = info[0]
    for i in range(1, len(info), 2):
        if info[i] == -1:
            break
        v, c = info[i], info[i + 1]
        tree[u].append((c, v))

mx_foot = 0
final_node = None
q = deque([(1, 0)])
v = [0] * (n + 1)
v[1] = 1
while q:
    cur, foot = q.popleft()
    if mx_foot < foot:
        mx_foot = foot
        final_node = cur
    for nc, nx in tree[cur]:
        if v[nx]:
            continue
        v[nx] = 1
        q.append((nx, foot + nc))

q2 = deque([(final_node, 0)])
v2 = [0] * (n + 1)
v2[final_node] = 1
while q2:
    cur, foot = q2.popleft()
    if mx_foot < foot:
        mx_foot = foot
    for nc, nx in tree[cur]:
        if v2[nx]:
            continue
        v2[nx] = 1
        q2.append((nx, foot + nc))

print(mx_foot)