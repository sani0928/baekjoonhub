import sys
input = sys.stdin.readline

def heart():
    for j in range(n):
        for i in range(n):
            if board[i][j] == '*':
                check = 0
                for k in range(4):
                    ni, nj = i + dr[k], j + dc[k]
                    if 0 > ni or n <= ni or 0 > nj or n <= nj:
                        break
                    if board[ni][nj] == '*':
                        check += 1
                    else:
                        break
                if check == 4:
                    return i, j

def length(sr, sc, d, again):
    l = 0
    r, c = sr + dr[d], sc + dc[d]
    while board[r][c] == '*':
        l += 1
        if 0 > r + dr[d] or n <= r + dr[d] or 0 > c + dc[d] or n <= c + dc[d]:
            break
        if board[r + dr[d]][c + dc[d]] != '*':
            break
        r, c = r + dr[d], c + dc[d]
    if again:
        left = length(r, c - 1, 1, 0)
        right = length(r, c + 1, 1, 0)
        return l, left, right
    return l

# 상, 하, 좌, 우
dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)
n = int(input())
board = [list(map(str, input().rstrip())) for _ in range(n)]
heart_r, heart_c = heart()
print(heart_r + 1, heart_c + 1)
ans1 = length(heart_r, heart_c, 2, 0)
ans2 = length(heart_r, heart_c, 3, 0)
ans3, ans4, ans5 = length(heart_r, heart_c, 1, 1)
print(ans1, ans2, ans3, ans4, ans5)