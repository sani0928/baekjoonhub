def solve():
    n = int(input())
    if n <= 4:
        if n == 2:
            return 'CY'
        else:
            return 'SK'

    # 1 = SK승, 0 = CY승
    dp = [1] * (n + 1)
    dp[2] = 0
    for i in range(1, n - 3):
        # 홀차례
        if i % 2 != 0:
            if dp[i + 3] == 0 or dp[i + 1] == 0 or dp[i] == 0:
                dp[i + 4] = 1
                continue
            dp[i + 4] = 0
        # 짝차례
        else:
            if dp[i + 3] == 1 and dp[i + 1] == 1 and dp[i] == 1:
                dp[i + 4] = 0
                continue
            dp[i + 4] = 1

    if dp[n] == 1:
        return 'SK'
    return 'CY'

if __name__ == '__main__':
    print(solve())