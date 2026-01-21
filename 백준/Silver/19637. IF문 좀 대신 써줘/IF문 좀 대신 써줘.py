import sys
input = sys.stdin.readline
def search(power):
    l, r = 0, len(upper)
    while l < r:
        mid = (l + r) // 2
        if upper[mid] >= power:
            r = mid
            continue
        l = mid + 1
    i = l
    return title[i]

n, m = map(int, input().split())
title, upper = [], []
for _ in range(n):
    t, u = input().split()
    u = int(u)
    if not upper or upper[-1] != u:
        title.append(t)
        upper.append(u)
for _ in range(m):
    print(search(int(input())))