import sys; sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def build(i, l, r):

    if l == r:
        tree[i] = num[l]
        return tree[i]

    mid = (l + r) // 2
    m1 = build(2 * i, l, mid)
    m2 = build(2 * i + 1, mid + 1, r)
    tree[i] = (m1 * m2) % MOD
    return tree[i]

def rebuild(i, l, r, qi, new):

    if qi < l or qi > r:
        return tree[i]

    if l == r:
        if l == qi:
            tree[i] = new
        return tree[i]

    mid = (l + r) // 2
    x = rebuild(2 * i, l, mid, qi, new)
    y = rebuild(2 * i + 1, mid + 1, r, qi, new)
    tree[i] = (x * y) % MOD
    return tree[i]

def query(i, l, r, ql, qr):

    if r < ql or l > qr:
        return 1

    if ql <= l and r <= qr:
        return tree[i]

    mid = (l + r) // 2
    x = query(2 * i, l, mid, ql, qr)
    y = query(2 * i + 1, mid + 1, r, ql, qr)
    return (x * y) % MOD

MOD = 10**9 + 7
N, M, K = map(int, input().split())
tree = [0] * (N * 4)
num = [0] + [int(input()) % MOD for _ in range(N)]
build(1, 1, N)

for _ in range(M + K):
    a, b, c = map(int, input().split())
    if a == 1:
        rebuild(1, 1, N, b, c % MOD)
    else:
        print(query(1, 1, N, b, c))