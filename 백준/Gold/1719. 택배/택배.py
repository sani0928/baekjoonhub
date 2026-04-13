import heapq

INF = float('inf')
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))
    graph[v].append((w, u))
for s in range(1, n + 1):
    hq = []
    res = ['-'] * (n + 1)
    dist = [INF] * (n + 1)
    dist[s] = 0
    heapq.heappush(hq, (0, s, 0))
    while hq:
        total, cur, f = heapq.heappop(hq)
        if total > dist[cur]:
            continue
        for cost, nx in graph[cur]:
            nx_cost = total + cost
            if nx_cost >= dist[nx]:
                continue
            dist[nx] = nx_cost
            if cur == s:
                res[nx] = nx
                heapq.heappush(hq, (nx_cost, nx, nx))
            else:
                res[nx] = f
                heapq.heappush(hq, (nx_cost, nx, f))
    print(*res[1:])