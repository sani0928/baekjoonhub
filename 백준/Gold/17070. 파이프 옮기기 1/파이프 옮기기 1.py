import sys
input = sys.stdin.readline
N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
if grid[N-1][N-1] == 1:
    print(0)
    exit()
H, D, V = 0, 1, 2

def go(r, c, dir):

    if r == N - 1 and c == N - 1:
        return 1

    if r == N - 1 and not c == N - 1 and dir == V:
        return 0

    if c == N - 1 and not r == N - 1 and dir == H:
        return 0

    cnt = 0

    # 가로 혹은 대각선일 때 오른쪽 이동
    if dir in (H, D):
        nc = c + 1
        if nc < N and grid[r][nc] != 1:
            cnt += go(r, nc, H)

    # 세로 혹은 대각선일 때 아래 이동
    if dir in (V, D):
        nr = r + 1
        if nr < N and grid[nr][c] != 1:
            cnt += go(nr, c, V)

    # 3칸 모두 빈칸이면 대각선 이동
    nr, nc = r + 1, c + 1
    if nr < N and nc < N:
        if grid[r][c+1] == 0 and grid[r+1][c] == 0 and grid[nr][nc] == 0:
            cnt += go(nr, nc, D)

    return cnt

print(go(0, 1, H))