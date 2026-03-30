import sys
input = sys.stdin.readline

dv = [(0, -1, -1, -1, 0, 1, 1, 1), (-1, -1, 0, 1, 1, 1, 0, -1)]
dv2 = [(-1, 0, 1, 0), (0, -1, 0, 1)]
N = 4
M, S = map(int, input().split())
fishes = [[[] for _ in range(N)] for _ in range(N)]
smells = [[0] * N for _ in range(N)]
for _ in range(M):
    r, c, direct = map(int, input().split())
    fishes[r-1][c-1].append(direct-1)
sr, sc = map(int, input().split())
sr -= 1
sc -= 1

def saving():
    temp = [[[] for _ in range(N)] for _ in range(N)]
    for x in range(N):
        for y in range(N):
            if not fishes[x][y]:
                continue
            temp[x][y] = fishes[x][y][:]
    return temp

def fish_move():
    new_fishes = [[[] for _ in range(N)] for _ in range(N)]
    for x in range(N):
        for y in range(N):
            if not fishes[x][y]:
                continue
            for d in fishes[x][y]:
                trying = 0
                nx, ny = x + dv[0][d], y + dv[1][d]
                while trying < 8:
                    if 0 <= nx < N and 0 <= ny < N and not smells[nx][ny] and not (sr == nx and sc == ny):
                        break
                    d = (d - 1) % 8
                    nx, ny = x + dv[0][d], y + dv[1][d]
                    trying += 1
                if trying < 8:
                    new_fishes[nx][ny].append(d)
                else:
                    new_fishes[x][y].append(d)
    return new_fishes

def shark_move():
    def recur(cnt, path, cx, cy):
        nonlocal best
        if len(path) == 3:
            if best == (-1, -1, -1, -1) or (-cnt, path) < (-best[0], best[1]):
                best = (cnt, path, cx, cy)
            return
        for k in range(4):
            nx, ny = cx + dv2[0][k], cy + dv2[1][k]
            if 0 > nx or 0 > ny or N <= nx or N <= ny:
                continue
            get = 0
            first = False
            if not vis[nx][ny]:
                vis[nx][ny] = 1
                get += len(fishes[nx][ny])
                first = True
            recur(cnt + get, path + [k], nx, ny)
            if first:
                vis[nx][ny] = 0

    best = (-1, -1, -1, -1)
    vis = [[0] * N for _ in range(N)]
    recur(0, [], sr, sc)
    x, y = sr, sc
    for d in best[1]:
        x, y = x + dv2[0][d], y + dv2[1][d]
        if fishes[x][y]:
            fishes[x][y] = []
            smells[x][y] = 3
    return best[2], best[3]

def decrease_smells():
    for x in range(N):
        for y in range(N):
            if not smells[x][y]:
                continue
            smells[x][y] -= 1
    return

def magic():
    for x in range(N):
        for y in range(N):
            if not save[x][y]:
                continue
            for d in save[x][y]:
                fishes[x][y].append(d)
    return

for t in range(S):
    save = saving() # 1
    fishes = fish_move() # 2
    sr, sc = shark_move() # 3
    decrease_smells() # 4
    magic() # 5

print(sum(len(fishes[x][y]) for x in range(N) for y in range(N)))