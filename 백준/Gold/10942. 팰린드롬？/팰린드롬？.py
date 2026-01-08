import sys
input = sys.stdin.readline

N = int(input())
arr = [0] + list(map(int, input().split()))
dp = [[0] * (N + 1) for _ in range(N + 1)]
# 하나일 때
for i in range(1, N + 1):
    dp[i][i] = 1
# 둘일 때
for i in range(1, N):
    if arr[i] == arr[i + 1]:
        dp[i][i + 1] = 1
# 셋 이상일 때
for l in range(2, N):
    for i in range(1, N - l + 1):
        if arr[i] == arr[l + i] and dp[i + 1][l + i - 1]:
            dp[i][l + i] = 1

# for row in dp:
#     print(*row)

M = int(input())
for _ in range(M):
    s, e = map(int, input().split())
    print(dp[s][e])