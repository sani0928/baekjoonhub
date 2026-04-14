import sys, heapq
input = sys.stdin.readline

INF = 10**9
ans = 10**9
v, e = map(int, input().split())
graph = [[] for _ in range(v + 1)]
for _ in range(e):
    a, b, w = map(int, input().split())
    graph[a].append((w, b))

for s in range(1, v + 1):
    dist = [INF] * (v + 1)
    dist[s] = 0
    hq = []
    heapq.heappush(hq, (0, s))
    while hq:
        curd, cur = heapq.heappop(hq)
        if curd >= ans or curd > dist[cur]: continue
        for cost, nx in graph[cur]:
            nxd = curd + cost
            if nxd >= ans: continue
            if nx == s:
                ans = min(ans, nxd)
                continue
            if nxd >= dist[nx]: continue
            dist[nx] = nxd
            heapq.heappush(hq, (nxd, nx))
print(ans if ans != 10**9 else -1)