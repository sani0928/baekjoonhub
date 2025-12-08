from collections import deque
from itertools import combinations

dr, dc = (0,1,0,-1), (1,0,-1,0)
def bfs(br_lst, left_blank):
    q = deque()
    visited = [[False] * N for _ in range(N)]
    for r, c in br_lst:
        visited[r][c] = True
        q.append((r, c))
    t = 0

    while q:
        if left_blank == 0:
            break
        for _ in range(len(q)):
            cr, cc = q.popleft()
            for k in range(4):
                nr, nc = cr + dr[k], cc + dc[k]
                if 0 <= nr < N and 0 <= nc < N:
                    if not visited[nr][nc]:
                        if grid[nr][nc] == 0:
                            left_blank -= 1
                            visited[nr][nc] = True
                            q.append((nr, nc))
                        elif grid[nr][nc] == 2:
                            visited[nr][nc] = True
                            q.append((nr, nc))
        t += 1

    if left_blank != 0:
        return -1

    return t

def searching():
    setlist, cnt = set(), 0
    for r in range(N):
        for c in range(N):
            if grid[r][c] == 2:
                setlist.add((r, c))
            elif grid[r][c] == 0:
                cnt += 1
    return setlist, cnt

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
ans = 50*50
br, blank = searching()
if blank == 0:
    print(0)
else:
    for lst in combinations(br, M):
        time = bfs(lst, blank)
        if time != -1:
            ans = min(ans, time)
    print(ans if ans != 50*50 else -1)