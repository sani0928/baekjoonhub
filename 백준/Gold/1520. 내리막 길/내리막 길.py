import sys; sys.setrecursionlimit(10 ** 6)
dr, dc = (0, 1, 0, -1), (1, 0, -1, 0)

M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(M)]
dp = [[-1] * N for _ in range(M)]

def dfs(cr, cc):

    if cr == M - 1 and cc == N - 1:
        return 1
    if dp[cr][cc] != -1:
        return dp[cr][cc]

    dp[cr][cc] = 0
    for k in range(4):
        nr, nc = cr + dr[k], cc + dc[k]
        if 0 <= nr < M and 0 <= nc < N and board[nr][nc] < board[cr][cc]:
            dp[cr][cc] += dfs(nr, nc)

    return dp[cr][cc]

ans = dfs(0, 0)
print(ans)