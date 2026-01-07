N, M = map(int, input().split())
dp = [0] * (N + 1)
for _ in range(M):
    day, page = map(int, input().split())
    for t in range(N, day - 1, -1):
        dp[t] = max(dp[t], dp[t - day] + page)
print(max(dp))