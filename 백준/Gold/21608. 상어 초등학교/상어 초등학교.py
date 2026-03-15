dr, dc = (0, 1, 0, -1), (1, 0, -1, 0)
n = int(input())
board = [[0] * n for _ in range(n)]
likes, order = {}, []
for _ in range(n*n):
    i, a, b, c, d = map(int, input().split())
    likes[i] = [a, b, c, d]
    order.append(i)

for x in order:
    candi = []
    for r in range(n):
        for c in range(n):
            if board[r][c] != 0:
                continue

            liked_cnt, blank_cnt = 0, 0
            for k in range(4):
                nr, nc = r + dr[k], c + dc[k]
                if 0 > nr or n <= nr or 0 > nc or n <= nc:
                    continue
                if board[nr][nc] in likes[x]:
                    liked_cnt += 1
                elif board[nr][nc] == 0:
                    blank_cnt += 1
            candi.append((-liked_cnt, -blank_cnt, r, c))
    candi.sort()
    board[candi[0][2]][candi[0][3]] = x

score = [0, 1, 10, 100, 1000]
ans = 0
for r in range(n):
    for c in range(n):
        cnt = 0
        x = board[r][c]
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 > nr or n <= nr or 0 > nc or n <= nc:
                continue
            if board[nr][nc] in likes[x]:
                cnt += 1
        ans += score[cnt]
print(ans)