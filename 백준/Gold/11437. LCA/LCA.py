import sys; from collections import deque
input = sys.stdin.readline

def solve():
    def search(a, b):
        while depth[a] != depth[b]:
            if depth[a] > depth[b]:
                a = parent[a]
            else:
                b = parent[b]
        while a != b:
            a = parent[a]
            b = parent[b]
        return a

    n = int(input())
    parent = list(range(n + 1))
    graph = [[] for _ in range(n + 1)]
    vis = [0] * (n + 1)
    depth = [0] * (n + 1)
    for _ in range(n - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    q = deque([(1, 0)])
    vis[1] = 1
    depth[1] = 0
    while q:
        cur, deep = q.popleft()
        for nx in graph[cur]:
            if vis[nx]:
                continue
            vis[nx] = 1
            depth[nx] = deep + 1
            parent[nx] = cur
            q.append((nx, deep + 1))

    for _ in range(int(input())):
        n1, n2 = map(int, input().split())
        print(search(n1, n2))

if __name__ == '__main__':
    solve()