import sys
input = sys.stdin.readline

R, C = map(int, input().split())
S = int(input())
stores = []
for _ in range(S):
    d, pos = map(int, input().split())
    if d == 1:
        x, y = pos, 0
    elif d == 2:
        x, y = pos, C
    elif d == 3:
        x, y = 0, pos
    else:
        x, y = R, pos
    stores.append((d, pos, x, y))

D, POS = map(int, input().split())
nearby, X, Y = set(), None, None
if D == 1 or D == 2:
    for n in range(3, 5):
        nearby.add(n)
    if D == 1:
        X, Y = POS, 0
    else:
        X, Y = POS, C
else:
    for n in range(1, 3):
        nearby.add(n)
    if D == 3:
        X, Y = 0, POS
    else:
        X, Y = R, POS

ans = 0
for store_dir, store_pos, store_x, store_y in stores:
    if store_dir == D:
       dist = abs(POS - store_pos)
       ans += dist
       continue
    if store_dir in nearby:
        dist = abs(store_x - X) + abs(store_y - Y)
        ans += dist
        continue
    if D == 1 or D == 2:
        dist = C + min(store_x + X, (R - X) + (R - store_x))
    else:
        dist = R + min(store_y + Y, (C - Y) + (C - store_y))
    ans += dist

print(ans)