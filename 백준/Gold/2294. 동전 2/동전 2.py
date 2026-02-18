INF = 10 ** 9
n, k = map(int, input().split())
dp = [INF] * (k + 1)
dp[0] = 0
for _ in range(n):
    coin = int(input())
    for i in range(coin, k + 1):
        dp[i] = min(dp[i - coin] + 1, dp[i])
print(dp[k] if dp[k] != INF else -1)