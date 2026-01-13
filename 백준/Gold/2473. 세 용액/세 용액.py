import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    ans = [arr[0], arr[1], arr[N - 1]]
    min_value = abs(sum(ans))

    for third in range(N - 2):
        l, r = third + 1, N - 1
        while l < r:
            value = arr[third] + arr[l] + arr[r]
            if min_value > abs(value):
                min_value = abs(value)
                ans = [arr[third], arr[l], arr[r]]

            if value < 0:
                l += 1
            elif value > 0:
                r -= 1
            else:
                return ans
    return ans

if __name__ == '__main__':
    print(*solve())