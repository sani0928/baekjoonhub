import sys
input = sys.stdin.readline

def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return 0
    if a < b:
        parent[b] = a
        return 1
    parent[a] = b
    return 1

def find(a):
    if a != parent[a]:
        parent[a] = find(parent[a])
    return parent[a]

n = int(input())
parent = list(range(n + 1))
node = [(0, 0)] + [list(map(float, input().split())) for _ in range(n)]
edges = []
for i in range(1, n + 1):
    x1, y1 = node[i]
    for j in range(i + 1, n + 1):
        x2, y2 = node[j]
        dist = (abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2) ** 0.5
        edges.append((dist, i, j))
edges.sort()
ans = 0
for d, n1, n2 in edges:
    if union(n1, n2):
        ans += d
print('{:.2f}'.format(ans))