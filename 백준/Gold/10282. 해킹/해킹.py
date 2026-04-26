from heapq import heappush, heappop; import sys
input = sys.stdin.readline

INF = 10**9
t = int(input())
for _ in range(t):
    total = 1
    n, d, c = map(int, input().split())
    dist = [INF] * (n + 1)
    dist[c] = 0
    hq = []
    heappush(hq, (0, c))
    graph = [[] for _ in range(n + 1)]
    for _ in range(d):
        a, b, s = map(int, input().split())
        graph[b].append((s, a))
    while hq:
        time, cur = heappop(hq)
        for t, nx in graph[cur]:
            if dist[nx] == INF:
                total += 1
            if dist[nx] <= time + t:
                continue
            dist[nx] = time + t
            heappush(hq, (time + t, nx))
    print(total, max(dist[i] for i in range(1, n + 1) if dist[i] != INF))