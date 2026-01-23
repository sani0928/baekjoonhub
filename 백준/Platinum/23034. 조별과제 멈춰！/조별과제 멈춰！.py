import sys
input = sys.stdin.readline

def solve():
    def union(nd1, nd2):
        nd1 = find(nd1)
        nd2 = find(nd2)
        if nd1 == nd2:
            return 0
        if size[nd1] < size[nd2]:
            nd1, nd2 = nd2, nd1
        parent[nd2] = nd1
        size[nd1] += nd2
        return 1

    def find(node):
        if node != parent[node]:
            parent[node] = find(parent[node])
        return parent[node]

    def total():
        res, cnt, mst = 0, 0, [[] for _ in range(n + 1)]
        for w, n1, n2 in edges:
            if union(n1, n2):
                res += w
                mst[n1].append((w, n2))
                mst[n2].append((w, n1))
                cnt += 1
                if cnt == n - 1:
                    return res, mst

    def dfs(start):
        vis = [0] * (n + 1)
        s = [start]
        vis[start] = 1
        while s:
            cur = s.pop()
            for w, nx in mst_graph[cur]:
                if not vis[nx]:
                    vis[nx] = 1
                    mx_edges[start][nx] = max(mx_edges[start][cur], w)
                    s.append(nx)

    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        a, b, c = map(int, input().split())
        edges.append((c, a, b))
    edges.sort()
    parent, size = list(range(n + 1)), [1] * (n + 1)
    mx_edges = [[0] * (n + 1) for _ in range(n + 1)]
    total_sum, mst_graph = total()
    for i in range(1, n + 1):
        dfs(i)

    q = int(input())
    for _ in range(q):
        x, y = map(int, input().split())
        print(total_sum - mx_edges[x][y])

if __name__ == '__main__':
    solve()