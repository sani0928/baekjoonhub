n = int(input())
graph = [tuple(map(int, input().split())) for _ in range(n)]
vis = [[0] * n for _ in range(n)]
s = [(node, node) for node in range(n)]
while s:
    start, cur = s.pop()
    for nx, i in enumerate(graph[cur]):
        if not i:
            continue
        if vis[start][nx]:
            continue
        vis[start][nx] = 1
        s.append((start, nx))
for row in vis:
    print(*row)