import sys

N = int(input())
lst = list(int(input()) for _ in range(N))
dp = [0] * N

if N == 1:
    print(lst[0])
    sys.exit(0)

elif N == 2:
    print(lst[0] + lst[1])
    sys.exit(0)

dp[0] = lst[0]
dp[1] = lst[0] + lst[1]
dp[2] = max(lst[0] + lst[2], lst[1] + lst[2])

for i in range(3, N):
    dp[i] = max(dp[i-2] + lst[i], dp[i-3] + lst[i-1] + lst[i])

ans = dp[-1]
print(ans)