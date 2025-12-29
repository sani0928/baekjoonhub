import sys
from collections import deque
input = sys.stdin.readline

def meetup(today_bird):
    # today: 오늘 갈 수 있는 경로, tomorrow: 얼음에 막혀서 내일 갈 수 있는 경로
    tomorrow_bird = deque()
    while today_bird:
        bird_r, bird_c = today_bird.popleft()
        for k in range(4):
            nr, nc = bird_r + dr[k], bird_c + dc[k]
            if 0 <= nr < R and 0 <= nc < C:
                if nr == birds[1][0] and nc == birds[1][1]:
                    return 'end'

                if not vis[nr][nc]:
                    if grid[nr][nc] == '.':
                        vis[nr][nc] = 1
                        today_bird.append((nr, nc))
                    elif grid[nr][nc] == 'X':
                        vis[nr][nc] = 1
                        tomorrow_bird.append((nr, nc))
    return tomorrow_bird

def melting(today_ice):
    # 얼음을 녹이면서 다음날 녹을 얼음 미리 수집
    tomorrow_ice = deque()
    while today_ice:
        r, c = today_ice.popleft()
        grid[r][c] = '.'
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 'X':
                if not ice_pos[nr][nc]:
                    ice_pos[nr][nc] = 1
                    tomorrow_ice.append((nr, nc))
    return tomorrow_ice

dr, dc = (0, 1, 0, -1), (1, 0, -1, 0)
R, C = map(int, input().split())
grid = []
birds = []
for r in range(R):
    row = list(input().rstrip())
    for c, ch in enumerate(row):
        if ch == 'L':
            birds.append((r, c))
            row[c] = '.'
    grid.append(row)
vis = [[0] * C for _ in range(R)]
bird_pos = deque([(birds[0][0], birds[0][1])])
# 초기 녹을 얼음 수집
ice = deque()
ice_pos = [[0] * C for _ in range(R)]
for r in range(R):
    for c in range(C):
        if grid[r][c] == 'X':
            for k in range(4):
                nr, nc = r + dr[k], c + dc[k]
                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == '.':
                    if not ice_pos[r][c]:
                        ice_pos[r][c] = 1
                        ice.append((r, c))
                        break
day = 0
while True:
    # 짝을 만나면 종료
    bird_pos = meetup(bird_pos)
    if bird_pos == 'end':
        break
    else:
        ice = melting(ice)
        day += 1

print(day)