def calcul(x, y):
    return abs(b[x][y] - b[x+h][y]) ** 2

h, w = map(int, input().split())
b = [tuple(map(int, input().split())) for _ in range(h*2)]
mn = [[float('inf')] * w for _ in range(h)]
for i in range(w):
    mn[0][i] = calcul(0, i)
for i in range(1, h):
    for j in range(w):
        value = calcul(i, j)
        for k in range(max(0, j - 1), min(w, j + 2)):
            mn[i][j] = min(mn[i][j], mn[i-1][k] + value)
print(min(mn[h-1]))