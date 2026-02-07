import sys
input = sys.stdin.readline

def solve():
    def test():
        nonlocal yes
        for t in range(t_cnt):
            for d in range(4):
                for r, c in t_range[t][d]:
                    if board[r][c] == 'O':
                        break
                    if board[r][c] =='S':
                        return
        yes = True
        return

    def recur(idx, cnt):
        if yes:
            return
        if cnt == 3:
            test()
            return

        for i in range(idx, b_cnt):
            r, c = blank[i]
            if board[r][c] == 'X':
                board[r][c] = 'O'
                recur(i + 1, cnt + 1)
                board[r][c] = 'X'


    dr, dc = (0, 1, 0, -1), (1, 0, -1, 0)
    blank, teacher = [], []
    t_cnt, b_cnt = 0, 0
    yes = False
    board = []

    n = int(input())
    for x in range(n):
        row = list(input().split())
        for y in range(n):
            if row[y] == 'T':
                t_cnt += 1
                teacher.append((x, y))
            elif row[y] == 'X':
                b_cnt += 1
                blank.append((x, y))
        board.append(row)

    t_range = [[[] for _ in range(4)] for _ in range(t_cnt)]
    for pos in range(t_cnt):
        tr, tc = teacher[pos]
        maxl = (n - 1 - tc, n - 1 - tr, tc, tr)
        for k in range(4):
            for l in range(1, maxl[k] + 1):
                nr, nc = tr + dr[k] * l, tc + dc[k] * l
                if board[nr][nc] == 'T':
                    break
                t_range[pos][k].append((nr, nc))

    recur(0, 0)
    return 'YES' if yes else 'NO'

if __name__ == '__main__':
    print(solve())