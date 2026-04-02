import sys
input = sys.stdin.readline

def convert(x, y):
    if type(x) == int:
        return chr(x + 65) + str(abs(int(y) - 8))
    return ord(x) - 65, abs(int(y) - 8)

data = list(input().split())
n = int(data[2])
data2 = [input().rstrip() for _ in range(n)]
king = list(convert(data[0][0], data[0][1]))
rock = list(convert(data[1][0], data[1][1]))

cmd = ['R', 'L', 'B', 'T', 'RT', 'LT', 'RB', 'LB']
dv = [
    (1, 0), (-1, 0), (0, 1), (0, -1),
    (1, -1), (-1, -1), (1, 1), (-1, 1)
]
for c in data2:
    d = cmd.index(c)
    nx, ny = king[0] + dv[d][0], king[1] + dv[d][1]
    if 0 > nx or 0 > ny or 8 <= nx or 8 <= ny:
        continue
    if nx == rock[0] and ny == rock[1]:
        nr2, ny2 = rock[0] + dv[d][0], rock[1] + dv[d][1]
        if 0 > nr2 or 0 > ny2 or 8 <= nr2 or 8 <= ny2:
            continue
        king[0], king[1] = nx, ny
        rock[0], rock[1] = nr2, ny2
        continue
    king[0], king[1] = nx, ny

print(convert(king[0], king[1]))
print(convert(rock[0], rock[1]))