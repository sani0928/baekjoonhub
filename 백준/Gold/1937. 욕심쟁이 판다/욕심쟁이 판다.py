dr, dc = (0,1,0,-1), (1,0,-1,0)
N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
dist = [[1] * N for _ in range(N)]

lst = [(grid[r][c], r, c) for r in range(N) for c in range(N)]
# 작은 음식부터 차근차근 +1
lst.sort()

for food, r, c in lst:
    for k in range(4):
        nr, nc = r + dr[k], c + dc[k]
        if 0 <= nr < N and 0 <= nc < N:
            if food < grid[nr][nc]:
                dist[nr][nc] = max(dist[nr][nc], dist[r][c]+ 1)

ans = max(map(max, dist))
print(ans)