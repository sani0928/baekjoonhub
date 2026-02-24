import sys
input = sys.stdin.readline

def is_bomb():
    global field
    def search_candi(r, c, color):
        nonlocal vis

        cnt = 1
        s = [(r, c)]
        rec = [(r, c)]
        vis[r][c] = 1
        while s:
            cr, cc = s.pop()
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = cr + dr, cc + dc
                if 0 > nr or 0 > nc or 12 <= nr or 6 <= nc:
                    continue
                if vis[nr][nc]:
                    continue
                if field[nr][nc] != color:
                    continue
                vis[nr][nc] = 1
                cnt += 1
                s.append((nr, nc))
                rec.append((nr, nc))

        if cnt >= 4:
            return rec
        return []

    expect = [] # 없어질 블록
    vis = [[0] * 6 for _ in range(12)] # 중복 탐색 방지 (search_candi 함수에 의존)
    for i in range(11, -1, -1):
        empty = 0
        for j in range(6):
            if field[i][j] != '.':
                expect += search_candi(i, j, field[i][j]) # 없어질 블록 수집
                continue
            empty += 1
        if empty == 6:
            break
    # 폭팔 후보가 있으면 다음턴(True), 없으면 종료(False)
    if expect:
        for x, y in expect:
            field[x][y] = '.'
        return True
    return False

def new_field():
    for c in range(6):
        bottom = 11 # 중력에 의해 블록이 내려갈 최상위 바닥
        while bottom > 0 and field[bottom][c] != '.':
            bottom -= 1
        if bottom == 0:
            continue
        for r in range(bottom - 1, -1, -1):
            if field[r][c] != '.':
                field[r][c], field[bottom][c] = field[bottom][c], field[r][c]
                bottom -= 1
    return

field = [list(input().rstrip()) for _ in range(12)]
ans = 0
while is_bomb():
    ans += 1
    new_field()
print(ans)