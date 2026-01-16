import sys
input = sys.stdin.readline

def solve():
    def union(x, y):
        x, y = find(x), find(y)
        if x == y:
            return 0
        if size[x] < size[y]:
            x, y = y, x
        size[x] += size[y]
        parent[y] = x
        return 1

    def find(x):
        if x != parent[x]:
            parent[x] = find(parent[x])
        return parent[x]

    def add_candi():
        lst = []
        for xyz in range(3):
            edges = [(nodes[i][xyz], i) for i in range(1, N + 1)]
            edges.sort()
            for j in range(1, N):
                c1, n1 = edges[j]
                c2, n2 = edges[j - 1]
                lst.append((abs(c1 - c2), n1, n2))
        lst.sort()
        return lst

    N = int(input())
    nodes = [(0, 0, 0)] + [tuple(map(int, input().split())) for _ in range(N)]
    parent = list(range(N + 1))
    candi = add_candi()
    size = [1] * (N + 1)
    ans, cnt = 0, 0
    for cost, a, b in candi:
        if union(a, b):
            ans += cost
            cnt += 1
            if cnt == N - 1:
                break
    return ans

if __name__ == '__main__':
    print(solve())