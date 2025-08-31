from collections import deque

N, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())

dr, dc = (0,1,0,-1), (1,0,-1,0)
lst = []
q = deque()

for i in range(N):
    for j in range(N):
        if grid[i][j] != 0:
            lst.append((grid[i][j], 0, i, j))

lst.sort()

for n, t, r, c in lst:
    q.append((n,t,r,c))

while q:

    num, time, r, c = q.popleft()

    if time == S:
        break

    for k in range(4):
        nr, nc = r + dr[k], c + dc[k]
        if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] == 0:
            grid[nr][nc] = num
            q.append((num, time + 1, nr, nc))

    # for chunk in grid:
    #     print(chunk)
    # print('---------------')

print(grid[X-1][Y-1])
