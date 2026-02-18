MOD = 10 ** 4 + 7
n = int(input())
dp = [list(range(11))] + [[0] * 11 for _ in range(n - 1)]
for i in range(1, n):
    for j in range(1, 11):
        dp[i][j] = dp[i][j-1] + dp[i-1][j]
print(dp[n - 1][10] % MOD)