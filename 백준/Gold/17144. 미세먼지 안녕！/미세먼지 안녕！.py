import sys
input = sys.stdin.readline

def solve():
    def spread():
        new_dust = []
        while dust:
            x, y, amount = dust.pop()
            cnt = 0
            for k in range(4):
                nx, ny = x + dr[k], y + dc[k]
                if 0 > nx or n <= nx or 0 > ny or m <= ny or board[nx][ny] == -1:
                    continue
                cnt += 1
                new_dust.append((nx, ny, amount // 5))
            if cnt != 0:
                board[x][y] -= (amount // 5) * cnt
        for x, y, amount in new_dust:
            board[x][y] += amount

    def up_blow(sx, sy):
        d = 0
        x, y = sx, sy
        while True:
            nx, ny = x + dr[d], y + dc[d]
            if 0 > nx or n <= nx or 0 > ny or m <= ny or nx > sx:
                d = (d + 1) % 4
                continue
            if board[nx][ny] == -1:
                return
            if board[x][y] != -1:
                board[x][y], board[nx][ny] = board[nx][ny], board[x][y]
            else:
                board[nx][ny] = 0
            x, y = nx, ny

    def down_blow(sx, sy):
        d = 2
        x, y = sx, sy
        while True:
            nx, ny = x + dr[d], y + dc[d]
            if 0 > nx or n <= nx or 0 > ny or m <= ny or nx < sx:
                d = (d - 1) % 4
                continue
            if board[nx][ny] == -1:
                return
            if board[x][y] != -1:
                board[x][y], board[nx][ny] = board[nx][ny], board[x][y]
            else:
                board[nx][ny] = 0
            x, y = nx, ny

    dr, dc = (-1, 0, 1, 0), (0, 1, 0, -1)
    n, m, t = map(int, input().split())
    board, dust = [], []
    up, down = None, None
    for r in range(n):
        row = list(map(int, input().split()))
        for c in range(m):
            if row[c] == 0:
                continue
            if row[c] == -1:
                if up:
                    down = (r, c)
                else:
                    up = (r, c)
            else:
                dust.append((r, c, row[c]))
        board.append(row)

    for turn in range(1, t + 1):
        spread() # 확산
        up_blow(up[0], up[1]) # 위로 순환
        down_blow(down[0], down[1]) # 아래로 순환
        if turn == t:
            return sum(num for row in board for num in row if num > 0)
        dust = [(r, c, board[r][c]) for r in range(n) for c in range(m) if board[r][c] > 0]

if __name__ == '__main__':
    print(solve())