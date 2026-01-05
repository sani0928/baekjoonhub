import sys
from collections import deque
input = sys.stdin.readline

dr, dc = (0, 1, 0, -1), (1, 0, -1, 0)
def check(x, y):
    # 갈 수 있는 길
    if matrix[x][y] == '.':
        return 1
    # 열 수 있는 문
    if matrix[x][y].isupper() and matrix[x][y].lower() in have_key:
        return 2
    # 열쇠
    if matrix[x][y].islower():
        # 새로운 열쇠
        if not matrix[x][y] in have_key:
            return 3
        return 1
    # 문서
    if matrix[x][y] == '$':
        return 4
    return 0

def entrance():

    flag = False
    docu_cnt = 0
    lst = []
    for x in range(H):
        if x == 0 or x == H - 1:
            yr = range(W)
        else:
            yr = (0, W - 1)

        for y in yr:
            avail = check(x, y)
            if not avail:
                continue

            if avail == 3:
                have_key.add(matrix[x][y])
                flag = True
                return lst, flag, docu_cnt

            elif avail == 4:
                docu_cnt += 1

            lst.append((x, y))

    return lst, flag, docu_cnt

def theft():

    q = deque()
    vis = [[0] * W for _ in range(H)]
    start, nx, docu_cnt = entrance()
    if nx:
        return nx, docu_cnt
    for r, c in start:
        q.append((r, c))
        vis[r][c] = 1

    while q:
        cr, cc = q.popleft()
        for k in range(4):
            nr, nc = cr + dr[k], cc + dc[k]
            if 0 <= nr < H and 0 <= nc < W and not vis[nr][nc]:
                avail = check(nr, nc)
                if avail:
                    # 새로운 키 획득 (bfs 종료)
                    if avail == 3:
                        nx = True
                        have_key.add(matrix[nr][nc])
                        return nx, docu_cnt
                    # 문서 획득
                    elif avail == 4:
                        docu_cnt += 1
                    vis[nr][nc] = 1
                    q.append((nr, nc))

    return nx, docu_cnt

T = int(input())
for _ in range(T):

    H, W = map(int, input().split())
    matrix = [list(map(str, input().rstrip())) for _ in range(H)]
    have_key = set(map(str, input().rstrip()))
    if '0' in have_key:
        have_key = set()

    while True:
        nx, ans = theft()
        # 새로 획득한 키가 없으면 종료
        if not nx:
            print(ans)
            break