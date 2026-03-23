s, c, o, n = map(int, input().split())
ts, tc = s + n, 2 * o + c
print(min(ts // 3, tc // 6))