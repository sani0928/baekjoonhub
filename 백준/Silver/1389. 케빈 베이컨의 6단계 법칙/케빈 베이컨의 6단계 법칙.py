import sys
from collections import deque
input = sys.stdin.readline

def solve():

    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        p1, p2 = map(int, input().split())
        graph[p1].append(p2)
        graph[p2].append(p1)

    def bfs(start):

        kevin_bacon = [0] * (n + 1)
        q = deque([(start, 0, start)])
        vis, check = [[0] * (n + 1) for _ in range(n + 1)], [[0] * (n + 1) for _ in range(n + 1)]
        vis[start][start], check[start][start] = 1, 1

        while q:
            cur, dist, target = q.popleft()

            if not vis[cur][cur]:
                vis[cur][cur] = 1
                q.append((cur, 0, cur))

            if not check[target][cur]:
                kevin_bacon[target] += dist

            for nx in graph[cur]:
                if vis[target][nx]:
                    continue
                vis[target][nx] = 1
                q.append((nx, dist + 1, target))

        return min(range(1, n + 1), key=lambda i: kevin_bacon[i])

    return bfs(1)

if __name__ == '__main__':
    print(solve())