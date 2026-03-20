import sys
input = sys.stdin.readline

def move():
    temp = []
    for x in range(N):
        for y in range(N):
            if not info[x][y]:
                continue
            for _ in range(len(info[x][y])):
                m, s, d = info[x][y].pop()
                nr, nc = x + dr[d] * s, y + dc[d] * s
                temp.append((nr % N, nc % N, m, s, d))
    for x, y, m, s, d in temp:
        info[x][y].append((m, s, d))

def divide():
    for x in range(N):
        for y in range(N):
            # 2개 이상의 파이어볼이 있는 칸
            if len(info[x][y]) >= 2:
                l = len(info[x][y])
                total_m = 0
                total_s = 0
                is_odd, is_even = True, True
                for _ in range(l):
                    m, s, d = info[x][y].pop()
                    total_m += m
                    total_s += s
                    if d % 2 == 0:
                        is_odd = False
                    else:
                        is_even = False
                # 질량이 0 이면 소멸
                if total_m // 5 == 0:
                    continue
                new_m = total_m // 5
                new_s = total_s // l
                for new_d in range(0 if is_odd or is_even else 1, 8, 2):
                    info[x][y].append((new_m, new_s, new_d))

dr, dc = (-1, -1, 0, 1, 1, 1, 0, -1), (0, 1, 1, 1, 0, -1, -1, -1)
N, M, K = map(int, input().split())
info = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    i1, i2, i3, i4, i5 = map(int, input().split())
    info[i1 - 1][i2 - 1].append((i3, i4, i5))
for _ in range(K):
    move()
    divide()

ans = 0
for r in range(N):
    for c in range(N):
        if info[r][c]:
            for i, _, _ in info[r][c]:
                ans += i
print(ans)