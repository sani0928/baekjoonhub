import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    parent = list(range(n + 1))
    in_dg = [0] * (n + 1)
    for _ in range(n - 1):
        a, b = map(int, input().split())
        in_dg[b] += 1
        parent[b] = a
    root = in_dg[1:].index(0) + 1
    x, y = map(int, input().split())
    y_fp = set()
    y_fp.add(y)
    while y != root:
        y = parent[y]
        y_fp.add(y)
    while not x in y_fp:
        x = parent[x]
    return x

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        print(solve())