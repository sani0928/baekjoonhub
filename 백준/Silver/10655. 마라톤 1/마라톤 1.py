import sys
input = sys.stdin.readline

n = int(input())
c = [tuple(map(int, input().split())) for _ in range(n)]
total = 0
cx, cy = c[0][0], c[0][1]
for i in range(1, n):
    total += abs(cx - c[i][0]) + abs(cy - c[i][1])
    cx, cy = c[i][0], c[i][1]
ans = 10 ** 9
for i in range(1, n - 1):
    diff = 0
    diff -= abs(c[i-1][0] - c[i][0]) + abs(c[i-1][1] - c[i][1])
    diff -= abs(c[i][0] - c[i+1][0]) + abs(c[i][1] - c[i+1][1])
    diff += abs(c[i-1][0] - c[i+1][0]) + abs(c[i-1][1] - c[i+1][1])
    ans = min(ans, total + diff)
print(ans)