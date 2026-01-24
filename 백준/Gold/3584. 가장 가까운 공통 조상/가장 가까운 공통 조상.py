import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    parent = list(range(n + 1))
    in_dg = [0] * n
    for _ in range(n - 1):
        a, b = map(int, input().split())
        in_dg[b - 1] += 1
        parent[b] = a
    root = in_dg.index(0) + 1
    x, y = map(int, input().split())
    x_fp = set()
    x_fp.add(x)
    while x != root:
        x = parent[x]
        x_fp.add(x)
    while not y in x_fp:
        y = parent[y]
    return y

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        print(solve())