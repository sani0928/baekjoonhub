import sys; input = sys.stdin.readline

def build(idx, l, r):
    def sort_lst(lst1, lst2):
        res = []
        x, y = 0, 0
        while x < len(lst1) and y < len(lst2):
            if lst1[x] <= lst2[y]:
                res.append(lst1[x])
                x += 1
            else:
                res.append(lst2[y])
                y += 1
        if x < len(lst1): res.extend(lst1[x:])
        if y < len(lst2): res.extend(lst2[y:])
        return res

    if l == r:
        tree[idx] = [arr[l]]
        return tree[idx]

    mid = (l + r) // 2
    a = build(2 * idx, l, mid)
    b = build(2 * idx + 1, mid + 1, r)
    tree[idx] = sort_lst(a, b)
    return tree[idx]

def binary_calcul(lst, k):
    l, r = 0, len(lst)
    while l < r:
        m = (l + r) // 2
        if lst[m] <= k:
            l = m + 1
        else:
            r = m
    return len(lst) - l

def search(idx, l, r, ql, qr, k):
    if qr < l or r < ql:
        return 0

    if ql <= l and r <= qr:
        return binary_calcul(tree[idx], k)

    mid = (l + r) // 2
    a = search(2 * idx, l, mid, ql, qr, k)
    b = search(2 * idx + 1, mid + 1, r, ql, qr, k)
    return a + b

N= int(input())
arr = tuple(map(int, input().split()))
M = int(input())

tree_l = 1
while tree_l < N:
    tree_l *= 2
tree = [[]] * (2 * tree_l)
build(1, 0, N - 1)
for _ in range(M):
    I, J, K = map(int, input().split())
    print(search(1, 0, N - 1, I - 1, J - 1, K))