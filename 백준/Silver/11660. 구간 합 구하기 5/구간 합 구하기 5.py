import sys
input = sys.stdin.readline
def prefix_sum(lx, ly, rx, ry):
    return prefix[rx][ry] - prefix[rx][ly-1] - prefix[lx-1][ry] + prefix[lx-1][ly-1]

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
prefix = [[0] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        prefix[i][j] = grid[i-1][j-1] + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    result = prefix_sum(x1, y1, x2, y2)
    print(result)