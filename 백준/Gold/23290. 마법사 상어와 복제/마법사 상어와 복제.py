import sys
input = sys.stdin.readline

fdv = [(0, -1, -1, -1, 0, 1, 1, 1), (-1, -1, 0, 1, 1, 1, 0, -1)]
sdv = [(-1, 0, 1, 0), (0, -1, 0, 1)]
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
    rec = [[[] for _ in range(N)] for _ in range(N)]
    for x in range(N):
        for y in range(N):
            if not fishes[x][y]:
                continue
            rec[x][y] = fishes[x][y][:]
    return rec

def fish_move():
    new_fishes = [[[] for _ in range(N)] for _ in range(N)]
    for x in range(N):
        for y in range(N):
            if not fishes[x][y]:
                continue
            for d in fishes[x][y]:
                trying = 0
                nx, ny = x + fdv[0][d], y + fdv[1][d]
                while trying < 8:
                    if 0 <= nx < N and 0 <= ny < N and not smells[nx][ny] and not (sr == nx and sc == ny):
                        break
                    d = (d - 1) % 8
                    nx, ny = x + fdv[0][d], y + fdv[1][d]
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
            if best is None or (-cnt, path) < (-best[0], best[1]):
                best = (cnt, path, cx, cy)
            return
        for k in range(4):
            nx, ny = cx + sdv[0][k], cy + sdv[1][k]
            if 0 > nx or 0 > ny or N <= nx or N <= ny:
                continue
            if not vis[nx][ny]:
                vis[nx][ny] = 1
                recur(cnt + len(fishes[nx][ny]), path + [k], nx, ny)
                vis[nx][ny] = 0
            else:
                recur(cnt, path + [k], nx, ny)
    best = None
    vis = [[0] * N for _ in range(N)]
    recur(0, [], sr, sc)

    x, y = sr, sc
    for d in best[1]:
        x, y = x + sdv[0][d], y + sdv[1][d]
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