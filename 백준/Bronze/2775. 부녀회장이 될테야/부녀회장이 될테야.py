T = int(input())
mx_h, mx_w = 0, 0
data = []
for _ in range(T):
    k, n = int(input()), int(input())
    mx_h, mx_w = max(mx_h, k + 1), max(mx_w, n)
    data.append((k, n))
dp = [[0] * mx_w for _ in range(mx_h)]
for i in range(mx_h):
    for j in range(mx_w):
        if i == 0:
            dp[i][j] = j + 1
            continue
        if j == 0:
            dp[i][0] = 1
            continue
        dp[i][j] = dp[i][j-1] + dp[i-1][j]
for k, n in data:
    print(dp[k][n - 1])