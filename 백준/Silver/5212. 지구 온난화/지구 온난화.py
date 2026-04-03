import sys
input = sys.stdin.readline

R, C = map(int, input().split())
og = [list(input().rstrip()) for _ in range(R)]
new = [['.'] * C for _ in range(R)]
t, d, l, r = 10**9, 0, 10**9, 0
for x in range(R):
    for y in range(C):
        if og[x][y] == '.': continue
        # sink or not
        water = 0
        for dx, dy in (0, 1), (1, 0), (0, -1), (-1, 0):
            nx, ny = x + dx, y + dy
            if 0 > nx or 0 > ny or R <= nx or C <= ny or og[nx][ny] == '.':
                water += 1
        if water >= 3: continue
        # resizing by unsinked island
        new[x][y] = 'X'
        t = min(t, x); d = max(d, x)
        l = min(l, y); r = max(r, y)

for i in range(t, d + 1):
    print(''.join(new[i][l : r + 1]))