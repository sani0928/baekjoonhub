import sys; sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def solve():
    def build(i, l, r):

        if l == r:
            tree[i] = num[l]
            return tree[i]

        mid = (l + r) // 2
        s1 = build(2 * i, l, mid)
        s2 = build(2 * i + 1, mid + 1, r)
        tree[i] = s1 + s2
        return tree[i]

    def search(i, ql, qr, l, r):

        if qr < l or r < ql:
            return 0

        if ql <= l and r <= qr:
            return tree[i]

        mid = (l + r) // 2
        s1 = search(2 * i, ql, qr, l, mid)
        s2 = search(2 * i + 1, ql, qr, mid + 1, r)
        return s1 + s2

    def rebuild(i, l, r, ci, diff):
        # 바뀐 자리와 관련 없는 범위는 return
        if ci < l or r < ci:
            return
        # 차이 반영
        tree[i] += diff
        if l == r:
            return
        mid = (l + r) // 2
        rebuild(2 * i, l, mid, ci, diff)
        rebuild(2 * i + 1, mid + 1, r, ci, diff)

    N, M, K = map(int, input().split())
    num = [0] + [int(input()) for _ in range(N)]
    tree = [0] * (4 * N)
    build(1, 1, N)
    for _ in range(M + K):
        a, b, c = map(int, input().split())
        if a == 1:
            difference = c - num[b]
            # 숫자 변경
            num[b] = c
            # b = 바뀐 자리, difference = 변화량
            rebuild(1, 1, N, b, difference)
            continue
        print(search(1, b, c, 1, N))

if __name__ == '__main__':
    solve()