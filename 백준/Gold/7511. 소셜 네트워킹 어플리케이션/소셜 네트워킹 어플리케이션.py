import sys
input = sys.stdin.readline

def solve():
    def union(x, y):
        x = find(x)
        y = find(y)
        if x == y:
            return 1
        if size[x] < size[y]:
            x, y = y, x
        size[x] += size[y]
        parent[y] = x
        return 0

    def find(x):
        while x != parent[x]:
            parent[x] = find(parent[x])
            x = parent[x]
        return x

    n = int(input())
    parent, size = list(range(n)), [1] * n
    k = int(input())
    for _ in range(k):
        a, b = map(int, input().split())
        union(a, b)

    m = int(input())
    for _ in range(m):
        u, v = map(int, input().split())
        if find(u) == find(v):
            print(1)
            continue
        print(0)

if __name__ == '__main__':
    t = int(input())
    for i in range(1, t + 1):
        print(f'Scenario {i}:')
        solve()
        print()