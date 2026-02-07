def solve():
    def is_possible(cr, cc, cl):
        for x in range(cr, cr + cl):
            for y in range(cc, cc + cl):
                if not board[x][y]:
                    return 0
        return 1

    def change_board(cr, cc, cl, status):
        for x in range(cr, cr + cl):
            for y in range(cc, cc + cl):
                board[x][y] = status
        return

    def recur(cnt):
        nonlocal ans

        if ans <= cnt:
            return

        r, c = None, None
        found = False
        for i in range(10):
            for j in range(10):
                if board[i][j]:
                    found = True
                    r, c = i, j
                    break
            if found:
                break
        if not found:
            ans = min(ans, cnt)
            return

        # 5부터 1까지 재귀
        maxl = min(5, min(10 - r, 10 - c))
        for l in range(maxl, 0, -1):
            if r + l > 10 or c + l > 10:
                continue
            if paper[l] == 0:
                continue
            if not is_possible(r, c, l):
                continue
            change_board(r, c, l, 0)
            paper[l] -= 1
            recur(cnt + 1)
            paper[l] += 1
            change_board(r, c, l, 1)
        return

    board = [list(map(int, input().split())) for _ in range(10)]
    ans, paper = 10 ** 9, [5] * 6
    recur(0)
    return ans if ans != 10 ** 9 else -1

if __name__ == '__main__':
    print(solve())