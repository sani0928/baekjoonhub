import sys
import heapq
input = sys.stdin.readline
def go(start_list, limit):
    global min_dist

    check = [0] * (V + 1)
    hq = []
    dist = [10 ** 9] * (V + 1)

    for s in start_list:
        heapq.heappush(hq, (0, s))
        dist[s] = 0

    while hq:

        cdist, cur = heapq.heappop(hq)

        if cdist != dist[cur]:
            continue

        if cdist > limit:
            continue

        if cur not in start_list and cdist <= limit and check[cur] == 0:
            check[cur] = 1
            min_dist[cur] += cdist

        for d, nx in graph[cur]:
            if dist[nx] > cdist + d:
                dist[nx] = cdist + d
                heapq.heappush(hq, (cdist + d, nx))
    return check

V, E = map(int, input().split())
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))
    graph[v].append((w, u))
M, x = map(int, input().split())
mac = set(map(int, input().split()))
S, y = map(int, input().split())
star = set(map(int, input().split()))
start = list(range(1, V + 1))
ans = 10**9
min_dist = [0] * (V + 1)
check1 = go(mac, x)
check2 = go(star, y)
for i in range(1, V + 1):
    if check1[i] and check2[i]:
        ans = min(ans, min_dist[i])
print(ans if ans != 10 ** 9 else -1)