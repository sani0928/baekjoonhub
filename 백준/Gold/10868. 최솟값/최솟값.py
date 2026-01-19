import sys
input = sys.stdin.readline

def build(i, l, r):
    # 최하위 노드 값
    if l == r:
        tree[i] = num[l]
        return tree[i]
    # 각 범위 내 노드에 최솟값 삽입
    mid = (l + r) // 2
    min_l = build(2 * i, l, mid)
    min_r = build(2 * i + 1, mid + 1, r)
    tree[i] = min(min_l, min_r)
    return tree[i]

def search(i, ql, qr, l, r):
    # 범위 밖
    if qr < l or r < ql:
        return 10 ** 9 + 1
    # 포함
    if ql <= l and r <= qr:
        return tree[i]
    # 부분 포함
    mid = (l + r) // 2
    a = search(2 * i, ql, qr, l, mid)
    b = search(2 * i + 1, ql, qr, mid + 1, r)
    return min(a, b)

N, M = map(int, input().split())
num = [int(input()) for _ in range(N)]
tree = [0] * (4 * N)
build(1, 0, N - 1)
for _ in range(M):
    s, e = map(int, input().split())
    print(search(1, s - 1, e - 1, 0, N - 1))