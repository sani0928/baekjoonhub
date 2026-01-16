import sys
input = sys.stdin.readline

def solve(n):
    if n == 0:
        return 1, 0
    if n == 1:
        return 0, 1
    if n == 2:
        return 1, 1
    arr = [(0, 0)] * (n + 1)
    arr[1], arr[2] = (0, 1), (1, 1)
    for i in range(3, n + 1):
        cnt0, cnt1 = arr[i - 1][0] + arr[i - 2][0], arr[i - 1][1] + arr[i - 2][1]
        arr[i] = (cnt0, cnt1)
    return arr[n][0], arr[n][1]

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        print(*solve(N))