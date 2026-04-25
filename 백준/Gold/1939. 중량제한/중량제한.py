from heapq import heappush, heappop; import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))
s, e = map(int, input().split())
dist = [0] * (n + 1)
dist[s] = 10**9+1
hq = []
heappush(hq, (-(10**9+1), s))
while hq:
    cur_mxw, cur_x = heappop(hq)
    cur_mxw = -cur_mxw
    if cur_mxw < dist[cur_x]:
        continue
    if cur_x == e:
        print(dist[e])
        break
    for w, nx in graph[cur_x]:
        new_mxw = min(cur_mxw, w)
        if dist[nx] < new_mxw:
            dist[nx] = new_mxw
            heappush(hq, (-new_mxw, nx))