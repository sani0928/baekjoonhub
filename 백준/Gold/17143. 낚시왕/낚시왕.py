# 상하우좌
dr, dc = (0, -1, 1, 0, 0), (0, 0, 0, 1, -1)

def swimming():
    global shark

    new_shark = [[[] for _ in range(C)] for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if shark[r][c]:
                s, d, z = shark[r][c][0]
                nr, nc, nd = r, c, None
                # 상 or 하
                if d == 1 or d == 2:
                    # 상: -1, 하: +1
                    dsign = -1 if d == 1 else 1
                    nr, dsign = new_pos(r, dsign, s % (2 * (R - 1)), R)
                    nd = 1 if dsign == -1 else 2
                # 우 or 좌
                else:
                    # 우: +1, 좌: -1
                    dsign = -1 if d == 4 else 1
                    nc, dsign = new_pos(c, dsign, s % (2 * (C - 1)), C)
                    nd = 3 if dsign == 1 else 4
                # 한 셀엔 덩치가 가장 큰 상어만 존재
                if not new_shark[nr][nc]:
                    new_shark[nr][nc].append((s, nd, z))
                else:
                    if new_shark[nr][nc][0][2] < z:
                        new_shark[nr][nc][0] = (s, nd, z)
    shark = new_shark
    return

def new_pos(pos, dsign, s, l):
    # 반사 반영
    pos += s * dsign
    # 경계 밖이면 경계 안으로 넣기
    while pos < 0 or pos >= l:
        if pos < 0:
            # 0 기준
            pos = -pos
            dsign = 1
        else:
            # l-1길이 기준
            pos = 2 * (l - 1) - pos
            dsign = -1

    return pos, dsign

R, C, M = map(int, input().split())
ans = 0
shark = [[[] for _ in range(C)] for _ in range(R)]
# 초기 상어 위치
for _ in range(M):
    X, Y, S, D, Z = map(int, input().split())
    X -= 1
    Y -= 1
    shark[X][Y].append((S, D, Z))

for cur in range(C):
    # 오른쪽 이동 후 포획
    for r in range(R):
        if shark[r][cur]:
            ans += shark[r][cur][0][2]
            shark[r][cur].pop()
            break
    # 상어 이동
    swimming()
print(ans)