def solve():
    h, w = map(int, input().split())
    board = [[0] * w for _ in range(h)]
    block = list(map(int, input().split()))
    ans = 0
    for c, cell in enumerate(block):
        for r in range(h - 1, h - cell - 1, -1):
            board[r][c] = 1

    for r in range(h):
        check = False
        total = 0
        for c in range(w):
            if board[r][c] == 1:
                if check:
                    ans += total
                    total = 0
                check = True
                continue
            if check:
                total += 1
    print(ans)

if __name__ == '__main__':
    solve()