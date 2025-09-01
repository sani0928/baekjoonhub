from collections import deque
R, C = map(int, input().split())
grid = [list(map(str, input().strip())) for _ in range(R)]

visited = [[False] * C for _ in range(R)]
fire_lst = []
fire_map = [[False] * C for _ in range(R)]

dr, dc = (0, 1, 0, -1), (1, 0, -1, 0)

me_q = deque()
fire_q = deque()

for r in range(R):
    for c in range(C):
        if grid[r][c] == 'F':
            fire_q.append((r, c))
            fire_map[r][c] = True
        elif grid[r][c] == 'J':
            me_q.append((r, c))

time = 0

def go():
    global time

    while me_q:

        time += 1

        for _ in range(len(fire_q)):
            fire_r, fire_c = fire_q.popleft()
            for k in range(4):
                fire_nr, fire_nc = fire_r + dr[k], fire_c + dc[k]
                if 0 <= fire_nr < R and 0 <= fire_nc < C:
                    if grid[fire_nr][fire_nc] == '.' and not fire_map[fire_nr][fire_nc]:
                        fire_map[fire_nr][fire_nc] = True
                        fire_q.append((fire_nr, fire_nc))

        for _ in range(len(me_q)):
            me_r, me_c = me_q.popleft()
            if me_r == 0 or me_r == R - 1 or me_c == 0 or me_c == C - 1:
                return time
            for k2 in range(4):
                me_nr, me_nc = me_r + dr[k2], me_c + dc[k2]
                if 0 <= me_nr < R and 0 <= me_nc < C and not visited[me_nr][me_nc]:
                    if grid[me_nr][me_nc] == '.' and not fire_map[me_nr][me_nc]:
                        visited[me_nr][me_nc] = True
                        me_q.append((me_nr, me_nc))

    return 'IMPOSSIBLE'

print(go())