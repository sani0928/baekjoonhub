import sys
from collections import deque
input = sys.stdin.readline

def solve():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    ans = None
    total_sum = 10**9
    for _ in range(M):
        p1, p2 = map(int, input().split())
        graph[p1].append(p2)
        graph[p2].append(p1)

    for p in range(1, N + 1):
        kevin_bacon = 0
        q = deque([(p, 0)])
        vis, check = [0] * (N + 1), [0] * (N + 1)
        vis[p], check[p] = 1, 1
        while q:
            cur, dist = q.popleft()
            if not check[cur]:
                kevin_bacon += dist
            for nx in graph[cur]:
                if vis[nx]:
                    continue
                vis[nx] = 1
                q.append((nx, dist + 1))
        if total_sum > kevin_bacon:
            total_sum = kevin_bacon
            ans = p
    print(ans)

if __name__ == '__main__':
    solve()