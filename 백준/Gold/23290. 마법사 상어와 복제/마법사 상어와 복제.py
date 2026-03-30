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
    temp = []
    for x in range(N):
        for y in range(N):
            if not fishes[x][y]:
                continue
            for d in fishes[x][y]:
                temp.append((x, y, d))
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
    candi = []
    s = [([], set(), 0, sr, sc)]
    while s:
        path, vis, cnt, cx, cy = s.pop()
        if len(path) == 3:
            candi.append((path, vis, cnt, cx, cy))
            continue
        for k in range(4):
            nx, ny = cx + dv2[0][k], cy + dv2[1][k]
            if 0 > nx or 0 > ny or N <= nx or N <= ny:
                continue
            new_vis = vis.copy()
            new_cnt = cnt
            if (nx, ny) not in vis:
                new_cnt += len(fishes[nx][ny])
                new_vis.add((nx, ny))
            s.append((path + [k], new_vis, new_cnt, nx, ny))

    candi.sort(key=lambda a: (-a[2], a[0]))
    best = candi[0]
    for x, y in best[1]:
        if not fishes[x][y]:
            continue
        fishes[x][y] = []
        smells[x][y] = 3
    return best[3], best[4]

def disappear_smells():
    for x in range(N):
        for y in range(N):
            if not smells[x][y]:
                continue
            smells[x][y] -= 1
    return

def magic():
    for x, y, d in save:
        fishes[x][y].append(d)
    return

for t in range(S):
    save = saving() # 1
    fishes = fish_move() # 2
    sr, sc = shark_move() # 3
    disappear_smells() # 4
    magic() # 5

print(sum(len(fishes[x][y]) for x in range(N) for y in range(N)))
