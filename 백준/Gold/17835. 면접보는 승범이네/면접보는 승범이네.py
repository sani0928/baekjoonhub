import sys; from heapq import *
input = sys.stdin.readline

INF = float('inf')
def solve():
    n, m, k = map(int, input().split())
    mn_d = [INF] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, c = map(int, input().split())
        graph[v].append((c, u))
    hq = []
    for i in map(int, input().split()):
        mn_d[i] = 0
        heappush(hq, (0, i))
    while hq:
        cost, cur = heappop(hq)
        if mn_d[cur] < cost: continue
        for nc, nx in graph[cur]:
            new_time = cost + nc
            if mn_d[nx] <= new_time: continue
            mn_d[nx] = new_time
            heappush(hq, (new_time, nx))
    spot, mx_d = 1, mn_d[1]
    for i in range(2, n + 1):
        if mx_d < mn_d[i]:
            mx_d = mn_d[i]
            spot = i
    print(spot, mx_d, sep='\n')
    return

if __name__ == '__main__':
    solve()