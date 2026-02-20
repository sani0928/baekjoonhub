import sys, heapq
input = sys.stdin.readline

n, m, k = map(int, input().split())
cities = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    cities[u].append((w, v))

hq = []
ans = [-1] * (n + 1)
order = [0] * (n + 1)
heapq.heappush(hq, (0, 1))
while hq:
    w, cur = heapq.heappop(hq)
    order[cur] += 1
    if order[cur] > k:
        continue
    if order[cur] == k:
        ans[cur] = w
    for d, nx in cities[cur]:
        if order[nx] < k:
            heapq.heappush(hq, (w + d, nx))

print('\n'.join(str(ans[i]) for i in range(1, n + 1)))