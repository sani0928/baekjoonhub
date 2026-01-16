def solve():
    cities = [tuple(map(int, input().split())) for _ in range(N)]
    max_idx = C + max(cities, key = lambda x : x[1])[1]
    dp = [10**9] * max_idx
    for i in range(N):
        dp[cities[i][1]] = min(dp[cities[i][1]], cities[i][0])

    ans = 10 ** 9
    for city in cities:
        cost, num = city[0], city[1]
        for n in range(num, max_idx):
            dp[n] = min(dp[n], dp[n - num] + cost)
            if n >= C:
                ans = min(ans, dp[n])
    return ans

if __name__ == '__main__':
    C, N = map(int, input().split())
    print(solve())