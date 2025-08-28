import sys

input = sys.stdin.readline

N, M = map(int, input().split())
woods = list(map(int, input().split()))
start, end = 0, max(woods)

while start <= end:

    cuting_h = (start + end) // 2
    have = 0

    for wood in woods:
        if wood > cuting_h:
            have += wood - cuting_h
        if have >= M:
            break

    if have >= M:
        start = cuting_h + 1
    else:
        end = cuting_h - 1

print(end)