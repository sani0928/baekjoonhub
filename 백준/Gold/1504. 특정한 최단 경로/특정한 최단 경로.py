import sys
import heapq

input = sys.stdin.readline
N, E = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(E):
    u, v, c = map(int, input().split())
    graph[u].append((v, c))
    graph[v].append((u, c))
v1, v2 = map(int, input().split())

def go(start):

    dist = [float('inf')] * (N + 1)
    dist[start] = 0
    # cost, u
    pq = [(dist[start], start)]

    while pq:

        cost, u = heapq.heappop(pq)

        if cost > dist[u]:
            continue

        for v, c in graph[u]:
            ncost = cost + c
            if ncost < dist[v]:
                dist[v] = ncost
                heapq.heappush(pq, (ncost, v))

    return dist

dist1 = go(1)
dist_v1 = go(v1)
dist_v2 = go(v2)
# print(dist1, dist_v1, dist_v2)
ans = min(dist1[v1] + dist_v1[v2] + dist_v2[N], dist1[v2] + dist_v2[v1] + dist_v1[N])
if ans == float('inf'):
    print(-1)
else:
    print(ans)