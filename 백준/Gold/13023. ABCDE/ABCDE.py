import sys
input = sys.stdin.readline

def solve():
    def recur(cur, dist):
        nonlocal end
        if end:
            return
        if dist == 4:
            end = True
            return
        v[cur] = 1
        for nx in graph[cur]:
            if not v[nx]:
                recur(nx, dist + 1)
        v[cur] = 0

    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    v = [0] * n
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    end = False
    for i in range(n):
        if end:
            return 1
        recur(i, 0)
    return 0

if __name__ == '__main__':
    print(solve())