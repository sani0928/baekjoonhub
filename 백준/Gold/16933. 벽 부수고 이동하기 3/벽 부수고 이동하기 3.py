import sys
from collections import deque
input = sys.stdin.readline

dr, dc = (0, 1, 0, -1), (1, 0, -1, 0)
N, M, K = map(int, input().split())
matrix = [list(map(int, input().rstrip())) for _ in range(N)]
vis = [[[[0] * M for _ in range(N)] for _ in range(K + 1)] for _ in range(2)]
vis[1][K][0][0] = 1
q = deque([(1, K, 0, 0)])
possible = False
while q:

    cnt, cut, cr, cc = q.popleft()
    if cr == N - 1 and cc == M - 1:
        possible = True
        print(cnt)
        break

    for k in range(4):
        nr, nc = cr + dr[k], cc + dc[k]
        if 0 <= nr < N and 0 <= nc < M and not vis[cnt % 2][cut][nr][nc]:
            if matrix[nr][nc]: # 벽이라면
                if cut > 0:
                    if cnt % 2 != 0: # 낮이라면
                        vis[cnt % 2][cut][nr][nc] = 1
                        q.append((cnt + 1, cut - 1, nr, nc))
                    else: # 밤이라면
                        vis[cnt % 2][cut][nr][nc] = 1
                        q.append((cnt + 1, cut, cr, cc))
            else: # 길이라면
                vis[cnt % 2][cut][nr][nc] = 1
                q.append((cnt + 1, cut, nr, nc))

if not possible:
    print(-1)