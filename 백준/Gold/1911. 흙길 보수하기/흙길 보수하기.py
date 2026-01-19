import sys
input = sys.stdin.readline

N, L = map(int, input().split())
coord = []
for _ in range(N):
    s, e = map(int, input().split())
    coord.append((s, e))
coord.sort()
ans, pos = 0, 0

for i in range(N):
    start, end = coord[i][0], coord[i][1]
    if pos > start:
        start = pos
    if start >= end:
        continue

    rest_len = end - start
    needed = (rest_len + L - 1) // L
    ans += needed
    pos = start + (L * needed)

print(ans)