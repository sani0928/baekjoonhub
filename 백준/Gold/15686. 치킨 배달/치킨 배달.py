from itertools import combinations

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

house = []
chicken_store = []

num = 1
for i in range(N):
    for j in range(N):
        if grid[i][j] == 1:
            house.append((i,j))
        elif grid[i][j] == 2:
            chicken_store.append((i,j))
            num += 1

comb = list(combinations(chicken_store, M))

ans = 10**9
for idx in range(len(comb)):
    more_nearby_len = 0
    for r, c in house:
        min_htoc = 10**9
        for r2, c2 in comb[idx]:
            min_htoc = min(min_htoc, abs(r-r2) + abs(c-c2))
        more_nearby_len += min_htoc

    ans = min(ans, more_nearby_len)

print(ans)