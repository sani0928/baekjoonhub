import sys
input = sys.stdin.readline

def solve():

    def build(i, l, r):
        if l == r:
            tree[i][0] = nums[l]
            tree[i][1] = nums[l]
            return tree[i][0], tree[i][1]

        mid = (l + r) // 2
        mn, mx = build(2 * i, l, mid)
        mn2, mx2 = build(2 * i + 1, mid + 1, r)
        tree[i][0], tree[i][1] = min(mn, mn2), max(mx, mx2)
        return tree[i][0], tree[i][1]

    def search(i, l, r, ql, qr):
        if l > qr or r < ql:
            return 10**9, 0

        if ql <= l and r <= qr:
            return tree[i][0], tree[i][1]

        mid = (l + r) // 2
        mn, mx = search(2 * i, l, mid, ql, qr)
        mn2, mx2 = search(2 * i + 1, mid + 1, r, ql, qr)
        return min(mn, mn2), max(mx, mx2)

    n, m = map(int, input().split())
    nums = [0] + list(int(input()) for _ in range(n))
    tree = [[0, 0] for _ in range(4 * n)]
    build(1, 1, n)
    for _ in range(m):
        a, b = map(int, input().split())
        print(*search(1, 1, n, a, b))

if __name__ == '__main__':
    solve()