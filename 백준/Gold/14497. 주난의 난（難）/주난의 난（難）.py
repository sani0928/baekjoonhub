import sys
input = sys.stdin.readline

dv = [(0, 1), (1, 0), (0, -1), (-1, 0)]
n, m = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())
x1, y1, x2, y2 = x1 - 1, y1 - 1, x2 - 1, y2 - 1
board = [list(input().rstrip()) for _ in range(n)]

s = [(x1, y1)]
vis = [[0] * m for _ in range(n)]
vis[x1][y1] = 1

ans, end = 0, 0
while True:
    nx = []
    while s:
        cr, cc = s.pop()
        for dr, dc in dv:
            nr, nc = cr + dr, cc+ dc
            if 0 > nr or 0 > nc or n <= nr or m <= nc or vis[nr][nc]:
                continue
            if nr == x2 and nc == y2:
                end = 1
                break
            vis[nr][nc] = 1
            if board[nr][nc] == '1':
                nx.append((nr, nc))
                continue
            s.append((nr, nc))
    ans += 1
    if end:
        break
    s = nx

print(ans)