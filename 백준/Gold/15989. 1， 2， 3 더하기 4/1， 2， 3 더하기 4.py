def solve():
    t = int(input())
    nums = list(int(input()) for _ in range(t))
    mx = max(nums)
    dp = [0] * (mx + 1)
    dp[0] = 1
    for s in (1, 2, 3):
        for i in range(s, mx + 1):
            dp[i] += dp[i - s]
    for i in range(t):
        print(dp[nums[i]])

if __name__ == '__main__':
    solve()