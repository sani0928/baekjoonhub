import heapq

def start_pos():

    for r in range(N):
        for c in range(M):
            if grid[r][c] == 2:
                return r, c
    return -1, -1

# 좌, 하, 상, 우
direct = [(0, -1), (1, 0), (-1, 0), (0, 1)]
N, M = map(int, input().split())
L, R = map(int, input().split())
grid = [list(map(int, input())) for _ in range(N)]
vis = [[0] * M for _ in range(N)]
sr, sc = start_pos()
vis[sr][sc] = 1
q = [(0, 0, sr, sc)]
heapq.heapify(q)
ans = 1

while q:
    curL, curR, cr, cc = heapq.heappop(q)

    if curL < L and curR < R:
        d = direct[:]
    elif curL < L and curR == R:
        d= direct[:3]
    elif curL == L and curR < R:
        d = direct[1:]
    else:
        d = direct[1:3]

    for dr, dc in d:
        nr, nc = cr + dr, cc + dc
        if 0 <= nr < N and 0 <= nc < M:
            if grid[nr][nc] != 1 and not vis[nr][nc]:
                if dr == 0 and dc == -1:
                    vis[nr][nc] = 1
                    ans += 1
                    heapq.heappush(q, (curL + 1, curR, nr, nc))
                elif dr == 0 and dc == 1:
                    vis[nr][nc] = 1
                    ans += 1
                    heapq.heappush(q, (curL, curR + 1, nr, nc))
                else:
                    vis[nr][nc] = 1
                    ans += 1
                    heapq.heappush(q, (curL, curR, nr, nc))

print(ans)