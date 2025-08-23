import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

grid = [list(map(str, input().strip())) for _ in range(N)]

dr, dc = (0, 1, 0, -1), (1, 0, -1, 0)

w_visited = [[False] * M for _ in range(N)]
s_visited = [[False] * M for _ in range(N)]

def checking_position():

    s_r, s_c = 0, 0
    wp = []

    for r in range(N):
        for c in range(M):
            if grid[r][c] == "*":
                wp.append((r, c))
            elif grid[r][c] == "S":
                s_r, s_c = r, c

    return wp, s_r, s_c

wp, sr, sc = checking_position()
# 물번짐 고려해서 '.'처리 (고슴도치 위치는 s_vistied에 기록되기 때문에 grid에 표시할 필요 X)
grid[sr][sc] = '.'

def go():

    wq = deque()
    for wr, wc in wp:
        wq.append((wr, wc))
        w_visited[wr][wc] = True

    sq = deque()
    sq.append((0, sr, sc))
    s_visited[sr][sc] = True

    while sq:
        # 물 먼저 확장
        # wq만큼 popleft를 해서 동시간 물번짐 보장
        wlength = len(wq)
        for _ in range(wlength):
            r1, c1 = wq.popleft()
            for k1 in range(4):

                nr1, nc1 = r1 + dr[k1], c1 + dc[k1]
                if 0 <= nr1 < N and 0 <= nc1 < M and grid[nr1][nc1] == '.' and not w_visited[nr1][nc1]:
                    w_visited[nr1][nc1] = True
                    wq.append((nr1, nc1))
        # 이후 고슴도치 이동
        slength = len(sq)
        for _ in range(slength):
            t, r2, c2 = sq.popleft()
            for k2 in range(4):

                nr2, nc2 = r2 + dr[k2], c2 + dc[k2]
                if 0 <= nr2 < N and 0 <= nc2 < M:

                    if grid[nr2][nc2] == 'D':
                        t = t + 1
                        return t

                    if grid[nr2][nc2] == '.' and not s_visited[nr2][nc2] and not w_visited[nr2][nc2]:
                        s_visited[nr2][nc2] = True
                        sq.append((t + 1, nr2, nc2))

        # print('---- 디버깅용 ----')
        # print(f'시간: ', t)
        # print(f'wq:', wq)
        # print(f'sq:', sq)
        # print('---- 물기록 ----')
        # for z in w_visited:
        #     print(*z)
        # print('---- 고슴도치기록 ----')
        # for zz in s_visited:
        #     print(*zz)
        # print('----------------')

    return "KAKTUS"

print(go())