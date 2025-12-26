import sys
input = sys.stdin.readline
dr, dc = (0, 1, 0, -1), (1, 0, -1, 0)
ans = 1
R, C = map(int, input().split())
matrix = [list(input().rstrip()) for _ in range(R)]
seen = {matrix[0][0]}

def back(cr, cc, cnt):
    global ans

    ans = max(ans, cnt)
    for k in range(4):
        nr, nc = cr + dr[k], cc + dc[k]
        if 0 <= nr < R and 0 <= nc < C:
            if not matrix[nr][nc] in seen:
                seen.add(matrix[nr][nc])
                back(nr, nc, cnt + 1)
                seen.remove(matrix[nr][nc])

back(0, 0, 1)
print(ans)