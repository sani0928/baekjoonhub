import sys
input = sys.stdin.readline

data = list(map(str, input().split()))
n = int(data[2])
data2 = [input().rstrip() for _ in range(n)]
king = [abs(int(data[0][1]) - 8), ord(data[0][0]) - 65]
rock = [abs(int(data[1][1]) - 8), ord(data[1][0]) - 65]

cmd = ['R', 'L', 'B', 'T', 'RT', 'LT', 'RB', 'LB']
dv = [
    (0, 1), (0, -1), (1, 0), (-1, 0),
    (-1, 1), (-1, -1), (1, 1), (1, -1)
]
for c in data2:
    d = cmd.index(c)
    nr, nc = king[0] + dv[d][0], king[1] + dv[d][1]
    if 0 > nr or 0 > nc or 8 <= nr or 8 <= nc:
        continue
    if nr == rock[0] and nc == rock[1]:
        nr2, nc2 = rock[0] + dv[d][0], rock[1] + dv[d][1]
        if 0 > nr2 or 0 > nc2 or 8 <= nr2 or 8 <= nc2:
            continue
        king[0], king[1] = nr, nc
        rock[0], rock[1] = nr2, nc2
        continue
    king[0], king[1] = nr, nc

print(chr(king[1] + 65) + str(abs(king[0] - 8)))
print(chr(rock[1] + 65) + str(abs(rock[0] - 8)))