T = int(input())
mx_h, mx_w = 0, 0
data = []
for _ in range(T):
    k, n = int(input()), int(input())
    mx_h, mx_w = max(mx_h, k), max(mx_w, n)
    data.append((k, n))
mx_h += 1
dp = [[0] * mx_w for _ in range(mx_h)]
for i in range(mx_w):
    dp[0][i] = i + 1
for i in range(1, mx_h):
    for j in range(mx_w ):
        dp[i][j] = dp[i][j-1] + dp[i-1][j]
for k, n in data:
    print(dp[k][n-1])