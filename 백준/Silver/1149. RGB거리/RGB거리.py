N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

dp = [[0, 0, 0] for _ in range(N)]

for idx in range(3):
    dp[0][idx] = lst[0][idx]

for i in range(1, N):
    for j in range(3):
        if j == 0:
            dp[i][j] = min(dp[i-1][1] + lst[i][0], dp[i-1][2] + lst[i][0])
        elif j == 1:
            dp[i][j] = min(dp[i-1][0] + lst[i][1], dp[i-1][2] + lst[i][1])
        else:
            dp[i][j] =min(dp[i-1][0] + lst[i][2], dp[i-1][1] + lst[i][2])

print(min(dp[-1]))