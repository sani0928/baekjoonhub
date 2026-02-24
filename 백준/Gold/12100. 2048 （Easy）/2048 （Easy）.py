import sys
input = sys.stdin.readline

def u(b):

    for c in range(n):
        pos = 0
        for r in range(pos + 1, n):
            if b[r][c] != 0:
                if b[pos][c] == 0:
                    b[r][c], b[pos][c] = b[pos][c], b[r][c]
                else:
                    if b[r][c] == b[pos][c]:
                        b[r][c] = 0
                        b[pos][c] *= 2
                        pos += 1
                    else:
                        pos += 1
                        b[r][c], b[pos][c] = b[pos][c], b[r][c]
    return b

def d(b):

    for c in range(n):
        pos = n - 1
        for r in range(pos - 1, -1, -1):
            if b[r][c] != 0:
                if b[pos][c] == 0:
                    b[r][c], b[pos][c] = b[pos][c], b[r][c]
                else:
                    if b[r][c] == b[pos][c]:
                        b[r][c] = 0
                        b[pos][c] *= 2
                        pos -= 1
                    else:
                        pos -= 1
                        b[r][c], b[pos][c] = b[pos][c], b[r][c]
    return b

def l(b):

    for r in range(n):
        pos = 0
        for c in range(pos + 1, n):
            if b[r][c] != 0:
                if b[r][pos] == 0:
                    b[r][c], b[r][pos] = b[r][pos], b[r][c]
                else:
                    if b[r][c] == b[r][pos]:
                        b[r][c] = 0
                        b[r][pos] *= 2
                        pos += 1
                    else:
                        pos += 1
                        b[r][c], b[r][pos] = b[r][pos], b[r][c]
    return b

def r(b):

    for r in range(n):
        pos = n - 1
        for c in range(pos - 1, -1, -1):
            if b[r][c] != 0:
                if b[r][pos] == 0:
                    b[r][c], b[r][pos] = b[r][pos], b[r][c]
                else:
                    if b[r][c] == b[r][pos]:
                        b[r][c] = 0
                        b[r][pos] *= 2
                        pos -= 1
                    else:
                        pos -= 1
                        b[r][c], b[r][pos] = b[r][pos], b[r][c]
    return b


def recur(board, cnt):
    global mx_val

    if cnt == 5:
        mx_val = max(mx_val, max(map(max, board)))
        return

    for dr in (u, d, l, r):
        new_board = [row[:] for row in board]
        dr(new_board)
        recur(new_board, cnt + 1)

n = int(input())
BOARD = [list(map(int, input().split())) for _ in range(n)]
mx_val = 0
recur(BOARD, 0)
print(mx_val)