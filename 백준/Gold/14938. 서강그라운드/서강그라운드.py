import sys, heapq
input = sys.stdin.readline

def search(f):
    hq = [(0, f)]
    dist = [float('inf')] * (n + 1)
    dist[f] = 0
    while hq:
        d, x = heapq.heappop(hq)
        if d != dist[x]:
            continue
        for w, nx in graph[x]:
            nd = d + w
            if nd > m:
                continue
            if nd >= dist[nx]:
                continue
            dist[nx] = nd
            heapq.heappush(hq, (nd, nx))
    return sum(cnt[node] for node in range(1, n + 1) if dist[node] <= m)

ans = 0
n, m, r = map(int, input().split())
cnt = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]
for _ in range(r):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))
for i in range(1, n + 1):
    ans = max(ans, search(i))
print(ans)