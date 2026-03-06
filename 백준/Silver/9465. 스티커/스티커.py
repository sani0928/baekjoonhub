import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    b = [list(map(int, input().split())) for _ in range(2)]
    if n == 1:
        print(max(b[0][0], b[1][0]))
        continue
    b[0][1] += b[1][0]
    b[1][1] += b[0][0]
    for i in range(2, n):
        b[0][i] = max(b[1][i - 1], b[1][i - 2]) + b[0][i]
        b[1][i] = max(b[0][i - 1], b[0][i - 2]) + b[1][i]
    print(max(b[0][n - 1], b[1][n - 1]))