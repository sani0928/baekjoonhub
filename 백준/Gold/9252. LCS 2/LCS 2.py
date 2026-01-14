import sys
input = sys.stdin.readline

def solve():
    char1 = [0] + list(input().rstrip())
    char2 = [0] + list(input().rstrip())
    char1_len = len(char1)
    char2_len = len(char2)
    dp = [[0] * char2_len for _ in range(char1_len)]

    for i in range(1, char1_len):
        for j in range(1, char2_len):
            if char1[i] == char2[j]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    lcs = []
    r, c = char1_len - 1, char2_len - 1
    print(dp[r][c])
    if dp[r][c]:
        while r > 0 and c > 0:
            if char1[r] == char2[c]:
                lcs.append(char1[r])
                r -= 1
                c -= 1
            else:
                if dp[r - 1][c] > dp[r][c - 1]:
                    r -= 1
                else:
                    c -= 1
    else:
        return
    lcs.reverse()
    print(''.join(lcs))

if __name__ == '__main__':
    solve()