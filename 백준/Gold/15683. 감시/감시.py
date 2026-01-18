import sys
input = sys.stdin.readline

def map_info():
    cctv_lst, wall_lst = [], []
    board = []
    blank, cnt = 0, 0
    for i in range(N):
        row = list(map(int, input().split()))
        for j in range(M):
            if not row[j]:
                blank += 1
                continue
            # 벽 위치 수집
            if row[j] == 6:
                wall_lst.append((i, j))
                continue
            # cctv 위치 수집
            cctv_lst.append((row[j], i, j))
            cnt += 1
        board.append(row)
    return board, cctv_lst, wall_lst, blank, cnt


def test(info):
    global ans

    def checking(n, idx, x, y):
        nr, nc = x + dr[n][idx], y + dc[n][idx]
        while 0 <= nr < N and 0 <= nc < M and office[nr][nc] != 6:
            if not (nr, nc) in cover and office[nr][nc] == 0:
                cover.add((nr, nc))
            nr, nc = nr + dr[n][idx], nc + dc[n][idx]

    cover = set()
    for num, k, r, c in info:
        if num == 1:
            checking(num, k, r, c)
            continue
            
        if num == 2:
            if k == 0:
                for i in range(2):
                    checking(num, i, r, c)
            else:
                for i in range(2, 4):
                    checking(num, i, r, c)
            continue
            
        if num == 3:
            for i in range(k, k + 2):
                checking(num, i, r, c)
            continue

        if num == 4:
            for i in range(k, k + 3):
                checking(num, i, r, c)
            continue

        if num == 5:
            for i in range(4):
                checking(num, i, r, c)
            continue

    ans = min(ans, spot - len(cover))
    return

def search(idx, total, lst):

    # 모든 cctv 각도 조정 완료
    if total == cctv_cnt:
        return test(lst)

    for i in range(idx, cctv_cnt):
        num, r, c = cctv[i]
        if not check[r][c]:
            for k in range(repeat[num]):
                check[r][c] = 1
                search(i + 1, total + 1, lst + [(num, k, r, c)])
                check[r][c] = 0

repeat = [0, 4, 2, 4, 4, 1]
dr = [[], (0, 1, 0, -1), (0, 0, -1, 1), (-1, 0, 1, 0, -1), (0, -1, 0, 1, 0, -1), (-1, 0, 1, 0)]
dc = [[], (1, 0, -1, 0), (-1, 1, 0, 0), (0, 1, 0, -1, 0),(-1, 0, 1, 0, -1, 0), (0, 1, 0, -1)]
N, M = map(int, input().split())
office, cctv, wall, spot, cctv_cnt = map_info()
check = [[0] * M for _ in range(N)]
ans = 10 ** 9
search(0, 0, [])
print(ans)