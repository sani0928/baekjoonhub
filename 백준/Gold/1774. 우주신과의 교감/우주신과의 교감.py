import sys
input = sys.stdin.readline

def add_candi():
    for i in range(1, N + 1):
        x1, y1 = node[i][0], node[i][1]
        for j in range(i + 1, N + 1):
            if find(i) == find(j):
                continue
            x2, y2 = node[j][0], node[j][1]
            dist = ((abs(x1 - x2)) ** 2 + (abs(y1 - y2) ** 2)) ** 0.5
            candi.append((dist, i, j))
    candi.sort()
    return

def find(a):
    if a != parent[a]:
        parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N, M = map(int, input().split())
node = [(-1, -1, -1)]
candi = [(-1, -1, -1)]
parent = list(range(N + 1))
size = [0] * (N + 1)
cnt = 0
for _ in range(1, N + 1):
    x, y = map(int, input().split())
    node.append((x, y))
for _ in range(M):
    u, v = map(int, input().split())
    if find(u) != find(v):
        union(u, v)
        cnt += 1
add_candi()

ans, cur = 0, 1
while cnt < N - 1:
    d, n1, n2 = candi[cur]
    if find(n1) != find(n2):
        union(n1, n2)
        ans += d
        cnt += 1
    cur += 1

print('{:.2f}'.format(ans))