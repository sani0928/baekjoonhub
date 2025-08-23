import sys
from collections import deque

input = sys.stdin.readline

N, M, T = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(N)]

INF = 100**9
dist = [[[INF] * 2 for _ in range(M)] for _ in range(N)]
dist[0][0][0] = 0

dr, dc = (0, 1, 0, -1), (1, 0, -1, 0)

# 순서대로 r, c, time, 명검 획득 여부
q = deque([(0, 0, 0, 0)])

while q:

    cr, cc, time, get = q.popleft()

    # 시간 초과 하면 실패
    if time > T:
        continue
    # 시간 내에 공주에게 도착 시 성공
    if cr == N - 1 and cc == M - 1:
        break

    if time > dist[cr][cc][get]:
        continue

    # 명검 획득 여부로 루트 갈림
    if grid[cr][cc] == 2:
        get = 1
    # 명검 없을 때 루트
    if get == 0:
        for k in range(4):
            nr, nc = cr + dr[k], cc + dc[k]
            if 0 <= nr < N and 0 <= nc < M and grid[nr][nc] != 1:
                if time + 1 < dist[nr][nc][get]:
                    dist[nr][nc][get] = time + 1
                    q.append((nr, nc, time + 1, 0))
    # 명검 있을 때 루트
    if get == 1:
        for k in range(4):
            nr, nc = cr + dr[k], cc + dc[k]
            if 0 <= nr < N and 0 <= nc < M:
                if time + 1 < dist[nr][nc][get]:
                    dist[nr][nc][get] = time + 1
                    q.append((nr, nc, time + 1, 1))

# 두 루트 중 더 짧은 거
ans = min(dist[N - 1][M - 1][0], dist[N - 1][M - 1][1])
print(ans if ans <= T else 'Fail')