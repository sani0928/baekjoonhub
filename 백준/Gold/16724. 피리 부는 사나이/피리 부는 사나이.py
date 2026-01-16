import sys
input = sys.stdin.readline

def search(cr, cc, num):
    global ans

    if g[cr][cc] == 'U':
        nr, nc = cr + dr[0], cc + dc[0]
    elif g[cr][cc] == 'D':
        nr, nc = cr + dr[1], cc + dc[1]
    elif g[cr][cc] == 'L':
        nr, nc = cr + dr[2], cc + dc[2]
    else:
        nr, nc = cr + dr[3], cc + dc[3]

    if check[nr][nc]:
        if check[nr][nc] == num:
            ans += 1
            return
        return

    if not check[nr][nc]:
        check[nr][nc] = num
        search(nr, nc, num)
    return
# 상하좌우
dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)
n, m = map(int, input().split())
g = [list(map(str, input().rstrip())) for _ in range(n)]
ans, turn = 0, 1
check = [[0] * m for _ in range(n)]
for r in range(n):
    for c in range(m):
        if check[r][c] != 0:
            continue
        check[r][c] = turn
        search(r, c, turn)
        turn += 1
print(ans)