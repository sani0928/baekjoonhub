import sys
input = sys.stdin.readline

dr, dc = (0, 1, 0, -1), (-1, 0, 1, 0)
left = [
    (-1, 0, 0.07), (1, 0, 0.07),
    (-2, 0, 0.02), (2, 0, 0.02),
    (-1, -1, 0.1), (1, -1, 0.1),
    (-1, 1, 0.01), (1, 1, 0.01),
    (0, -2, 0.05)
]
down = [(-y, x, radio) for x, y, radio in left]
right = [(x, -y, radio) for x, y, radio in left]
up = [(y, -x, radio) for x, y, radio in left]
move = [left, down, right, up]

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

def tornado():
    ans = 0
    cr, cc = n // 2, n // 2
    d = 0
    l = 1
    while True:
        for _ in range(2):
            for _ in range(l):
                # 다음 이동 위치로 갱신
                cr, cc = cr + dr[d], cc + dc[d]
                # 범위 밖 모래 갱신
                ans += splash(cr, cc, d)
                if cr == 0 and cc == 0:
                    return ans
            d = (d + 1) % 4
        l += 1

def splash(r, c, d):
    if not board[r][c]:
        return 0
    rest = board[r][c]
    out = 0
    for x, y, radio in move[d]:
        sand = int(board[r][c] * radio)
        nr, nc = r + x, c + y
        rest -= sand
        if 0 > nr or n <= nr or 0 > nc or n <= nc:
            out += sand
            continue
        # 비율에 맞게 모래 splash
        board[nr][nc] += sand
    # 모래를 다 흩날린 후 해당 위치 모래 비우기
    board[r][c] = 0
    # 남은 모래 알파 자리에 추가 (알파 자리가 범위 밖이면 out + rest)
    ax, ay = r + dr[d], c + dc[d]
    if 0 <= ax < n and 0 <= ay < n:
        board[ax][ay] += rest
        return out
    return out + rest

print(tornado())