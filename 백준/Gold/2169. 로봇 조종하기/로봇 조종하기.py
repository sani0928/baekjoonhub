N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
dp = [[-10**9] * M for _ in range(N)]

dp[0][0] = grid[0][0]
for i in range(1, M):
    dp[0][i] = dp[0][i-1] + grid[0][i]

for r in range(1, N):
    left = [-10**9] * M; right = [-10**9] * M

    left[0] = dp[r-1][0] + grid[r][0]
    for j in range(1, M):
        left[j] = max(left[j-1], dp[r-1][j]) + grid[r][j]

    right[M-1] = dp[r-1][M-1] + grid[r][M-1]
    for j in range(M-2, -1, -1):
        right[j] = max(right[j+1], dp[r-1][j]) + grid[r][j]
    # print(f'left : {left}, right : {right}')
    for c in range(M):
        dp[r][c] = max(left[c], right[c])

print(dp[N-1][M-1])