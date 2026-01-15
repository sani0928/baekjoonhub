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

    def bfs(s):

        kevin_bacon = [0] * (n + 1)
        q = deque([(s, s, 0)])
        vis = [[0] * (n + 1) for _ in range(n + 1)]
        vis[s][s] = 1, 1

        while q:
            target, cur, dist = q.popleft()

            if not vis[cur][cur]:
                vis[cur][cur] = 1
                q.append((cur, cur, 0))

            for nx in graph[cur]:
                if vis[target][nx]:
                    continue
                vis[target][nx] = 1
                kevin_bacon[target] += dist + 1
                q.append((target, nx, dist + 1))

        return min(range(1, n + 1), key=lambda i: kevin_bacon[i])

    return bfs(1)

if __name__ == '__main__':
    print(solve())