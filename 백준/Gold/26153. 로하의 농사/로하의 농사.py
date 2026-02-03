import sys
input = sys.stdin.readline

def solve():
    def search(cx, cy, rest, total, pipe):
        nonlocal ans

        if rest > 0:
            for dx, dy in pipe:
                nx, ny = cx + dx, cy + dy
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if v[nx][ny]:
                    continue
                if rest >= 1:
                    v[nx][ny] = 1
                    search(nx, ny, rest - 1, total + board[nx][ny], [(dx, dy)])
                    v[nx][ny] = 0
                if rest >= 2:
                    if dx == 0:
                        v[nx][ny] = 1
                        search(nx, ny, rest - 2, total + board[nx][ny], [(-1, 0), (1, 0)])
                        v[nx][ny] = 0
                    else:
                        v[nx][ny] = 1
                        search(nx, ny, rest - 2, total + board[nx][ny], [(0, -1), (0, 1)])
                        v[nx][ny] = 0
        ans = max(ans, total)

    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    x, y, p = map(int, input().split())
    v = [[0] * m for _ in range(n)]
    v[x][y] = 1
    ans = 0
    search(x, y, p, board[x][y], [(0, 1), (1, 0), (0, -1), (-1, 0)])
    print(ans)

if __name__ == '__main__':
    solve()