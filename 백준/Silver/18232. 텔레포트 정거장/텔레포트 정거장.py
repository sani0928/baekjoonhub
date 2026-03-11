import sys, heapq
input = sys.stdin.readline

n, m = map(int, input().split())
s, e = map(int, input().split())
gate = [[] for _ in range(n + 1)]
d = [float('inf')] * (n + 1)
for _ in range(m):
    x, y = map(int, input().split())
    gate[x].append(y)
    gate[y].append(x)
hq = [(0, s)]
while hq:
    time, cur = heapq.heappop(hq)
    if cur == e:
        break
    for nx in gate[cur]:
        if time + 1 < d[nx]:
            d[nx] = time + 1
            heapq.heappush(hq, (time + 1, nx))
    if cur - 1 >= 1 and time + 1 < d[cur - 1]:
        d[cur - 1] = time + 1
        heapq.heappush(hq, (time + 1, cur - 1))
    if cur + 1 <= n and time + 1 < d[cur + 1]:
        d[cur + 1] = time + 1
        heapq.heappush(hq, (time + 1, cur + 1))
print(d[e])