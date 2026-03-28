import sys; from collections import deque
input = sys.stdin.readline

def rotation(l):
    new = [[0] * LEN for _ in range(LEN)]
    for x in range(0, LEN, l):
        for y in range(0, LEN, l):
            for x2 in range(l):
                for y2 in range(l):
                    new[x + y2][y + l - 1 - x2] = board[x + x2][y + y2]
    return new

def check():
    candi = []
    for x in range(LEN):
        for y in range(LEN):
            if not board[x][y]:
                continue
            cnt = 0
            for dx, dy in dv:
                nx, ny = x + dx, y + dy
                if 0 > nx or 0 > ny or LEN <= nx or LEN <= ny or not board[nx][ny]:
                    continue
                cnt += 1
            if cnt < 3:
                candi.append((x, y))
    for x, y in candi:
        board[x][y] -= 1

def max_cnt():
    mx = 0
    vis = [[0] * LEN for _ in range(LEN)]
    for x in range(LEN):
        for y in range(LEN):
            if vis[x][y] or not board[x][y]:
                continue
            vis[x][y] = 1
            cnt = 1
            q = deque([(x, y)])
            while q:
                cr, cc = q.popleft()
                for dr, dc in dv:
                    nr, nc = cr + dr, cc + dc
                    if 0 > nr or 0 > nc or LEN <= nr or LEN <= nc or not board[nr][nc]:
                        continue
                    if vis[nr][nc]:
                        continue
                    vis[nr][nc] = 1
                    q.append((nr, nc))
                    cnt += 1
            mx = max(mx, cnt)
    return mx

dv = [(0, 1), (1, 0), (0, -1), (-1, 0)]
N, Q = map(int, input().split())
LEN = 2**N
board = [list(map(int, input().split())) for _ in range(LEN)]
q_seq = list(map(int, input().split()))

for i in q_seq:
    board = rotation(2**i)
    check()

print(sum(map(sum, board)), max_cnt(), sep='\n')