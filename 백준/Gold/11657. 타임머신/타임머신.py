import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    edges = []
    d = [float('inf')] * (n + 1)
    d[1] = 0
    for _ in range(m):
        a, b, c = map(int, input().split())
        edges.append((a, b, c))

    for cnt in range(n):
        for i in range(m):
            u, v, c = edges[i][0], edges[i][1], edges[i][2]
            if d[u] != float('inf') and d[v] > d[u] + c:
                d[v] = d[u] + c
                if cnt == n - 1:
                    print(-1)
                    return

    for i in range(2, n + 1):
        if d[i] == float('inf'):
            print(-1)
            continue
        print(d[i])

if __name__ == '__main__':
    solve()