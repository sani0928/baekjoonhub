def check(x, y):
    if b[x][0] == b[x][1] == b[x][2]: return 1
    if b[0][y] == b[1][y] == b[2][y]: return 1
    if b[0][0] == b[1][1] == b[2][2] == cur: return 1
    if b[0][2] == b[1][1] == b[2][0] == cur: return 1

cur = int(input())
b = [[0] * 3 for _ in range(3)]
turn = 1
while turn < 10:
    r, c = map(lambda x: int(x) - 1, input().split())
    b[r][c] = cur
    if turn >= 5 and check(r, c): break
    if cur == 2: cur = 1
    else: cur = 2
    turn += 1
print(cur if turn != 10 else 0)