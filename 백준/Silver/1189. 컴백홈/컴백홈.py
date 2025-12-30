def comebackhome(cur):
    global ans

    while cur:
        dist, cr, cc = cur.pop()
        if cr == 0 and cc == C - 1:
            if dist == K:
                ans += 1
            return
        for k in range(4):
            nr, nc = cr + dr[k], cc + dc[k]
            if 0 <= nr < R and 0 <= nc < C and matrix[nr][nc] != 'T':
                if not vis[nr][nc]:
                    vis[nr][nc] = 1
                    comebackhome(cur + [(dist + 1, nr, nc)])
                    vis[nr][nc] = 0
    return

dr, dc = (0, 1, 0, -1), (1, 0, -1, 0)
R, C, K = map(int, input().split())
matrix = [list(input().rstrip()) for _ in range(R)]
vis = [[0] * C for _ in range(R)]
vis[R - 1][0] = 1
start = [(1, R - 1, 0)]
ans = 0
comebackhome(start)
print(ans)