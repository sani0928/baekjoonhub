import sys
input = sys.stdin.readline

def spring():
    global trees, bye

    temp = [[[] for _ in range(N)] for _ in range(N)]
    bye = []

    for i in range(N):
        for j in range(N):
            for age in trees[i][j]:
                if food[i][j] < age:
                    bye.append((age, i, j))
                else:
                    food[i][j] -= age
                    temp[i][j].append(age + 1)
    trees = temp
    return

def summer():

    for dead_age, dead_r, dead_c in bye:
        food[dead_r][dead_c] += dead_age // 2
    return

def autumn():
    global trees

    temp = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for age in trees[i][j]:
                if age % 5 != 0:
                    continue
                for k in range(8):
                    nr, nc = i + dr[k], j + dc[k]
                    if 0 <= nr < N and 0 <= nc < N:
                        temp[nr][nc].append(1)

    for i in range(N):
        for j in range(N):
            temp[i][j] += trees[i][j]
    trees = temp
    return

def winter():

    for r in range(N):
        for c in range(N):
            food[r][c] += A[r][c]
    return

dr, dc = (0, 1, 1, 1, 0, -1, -1, -1), (1, 1, 0, -1, -1, -1, 0, 1)

N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
food = [[5] * N for _ in range(N)]
trees = [[[] for _ in range(N)] for _ in range(N)]
bye = []
time = 0

for _ in range(M):
    tree_r, tree_c, tree_age = map(int, input().split())
    trees[tree_r - 1][tree_c - 1].append(tree_age)

for r in range(N):
    for c in range(N):
        trees[r][c].sort()

while time != K:
    spring()
    summer()
    autumn()
    winter()
    time += 1

ans = 0
for r in range(N):
    for c in range(N):
        ans += len(trees[r][c])
print(ans)