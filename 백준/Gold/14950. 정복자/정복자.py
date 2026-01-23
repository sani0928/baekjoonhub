import sys
input = sys.stdin.readline

def union(a, b):
    a, b = find(a), find(b)
    if a == b:
        return 0
    if size[a] < size[b]:
        a, b = b, a
    size[a] += size[b]
    parent[b] = a
    return 1

def find(a):
    while a != parent[a]:
        parent[a] = parent[parent[a]]
        a = parent[a]
    return a

N, M, T = map(int, input().split())
edges, parent, size = [], list(range(N + 1)), [1] * (N + 1)
for _ in range(M):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))
edges.sort()
ans, cnt = 0, 0
for w, u, v in edges:
    if union(u, v):
        ans += w + (T * cnt)
        cnt += 1
        if cnt == N - 1:
            break
print(ans)