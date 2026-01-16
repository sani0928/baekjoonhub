import sys
input = sys.stdin.readline

def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        if x < y:
            parent[y] = x
        else:
            parent[x] = y
    return

def find(x):
    if x != parent[x]:
        return find(parent[x])
    return x

def add_edges(coord):

    lst = []
    for i in range(1, N + 1):
        lst.append((nodes[i][coord], i))
    lst.sort()
    for i in range(1, N):
        candi.append((abs(lst[i][0] - lst[i - 1][0]), lst[i][1], lst[i - 1][1]))
    return lst

N = int(input())
nodes = [(0, 0, 0)] + [tuple(map(int, input().split())) for _ in range(N)]
parent = list(range(N + 1))
candi = []
x_edges, y_edges, z_edges = add_edges(0), add_edges(1), add_edges(2)
candi.sort()
ans, cnt = 0, 0
while cnt < N - 1:
    for i in range(len(candi)):
        cost, a, b = candi[i]
        if find(a) == find(b):
            continue
        union(a, b)
        ans += cost
        cnt += 1
print(ans)