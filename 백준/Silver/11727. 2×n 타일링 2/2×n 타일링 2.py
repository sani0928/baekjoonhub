n = int(input())
if n == 1:
    print(1)
else:
    MOD = 10007
    dp = [0] * n
    dp[0], dp[1] = 1, 3
    for i in range(2, n):
        dp[i] = (2 * dp[i-2] + dp[i-1]) % MOD
    print(dp[-1])