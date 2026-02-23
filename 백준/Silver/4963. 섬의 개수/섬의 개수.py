import sys; input = sys.stdin.readline

def check(r, c):
    s = [(r, c)]
    while s:
        cr, cc = s.pop()
        for dr, dc in direct:
            nr, nc = cr + dr, cc+ dc
            if 0 > nr or 0 > nc or h <= nr or w <= nc:
                continue
            if board[nr][nc] == 0:
                continue
            if vis[nr][nc] == 1:
                continue
            vis[nr][nc] = 1
            s.append((nr, nc))
    return

direct = [
    (0, 1), (1, 1), (1, 0),
    (1, -1), (0, -1), (-1, -1),
    (-1, 0), (-1, 1)
]
while True:
    w, h = map(int, input().split())
    if (w, h) == (0, 0):
        break
    board = [list(map(int, input().split())) for _ in range(h)]
    vis = [[0] * w for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if  not vis[i][j] and board[i][j] == 1:
                ans += 1
                vis[i][j] = 1
                check(i, j)
    print(ans)