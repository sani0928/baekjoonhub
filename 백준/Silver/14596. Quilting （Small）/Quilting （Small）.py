def calcul(x, y):
    return abs(b[x][y] - b[x+h][y]) ** 2

ans = 10**9
h, w = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(h*2)]
s = []
for i in range(w):
    s.append((calcul(0, i), 0, i))
while s:
    cv, cr, cc = s.pop()
    if cv >= ans:
        continue
    if cr == h - 1:
        ans = min(ans, cv)
        continue
    for nc in range(max(0, cc - 1), min(w, cc + 2)):
        s.append((cv + calcul(cr + 1, nc), cr + 1, nc))
print(ans)