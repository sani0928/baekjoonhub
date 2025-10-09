from collections import deque

def searching_shark():

    for r in range(N):
        for c in range(N):
            if sea[r][c] == 9:
                return r, c
    return

def moving(sr, sc):
    global ans, cnt

    q = deque([(sr, sc, 0)])
    visited = [[False] * N for _ in range(N)]
    visited[sr][sc] = True

    candidates = []
    min_dist = None

    while q:

        cr, cc, time = q.popleft()
        # 최소거리보다 멀리 가면 무빙 중단
        if min_dist is not None and time > min_dist:
            break
        # 먹을 수 있는 물고기를 발견했다면 (가장 가까운)
        if 0 < sea[cr][cc] < shark_weight:
            candidates.append((cr,cc))
            min_dist = time
            continue

        for k in range(4):
            nr, nc = cr + dr[k], cc + dc[k]
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and sea[nr][nc] <= shark_weight:
                visited[nr][nc] = True
                q.append((nr, nc, time + 1))
    # 먹을게 있다면 가장 위, 가장 왼쪽 먹이 선택
    if candidates:
        nr, nc = min(candidates)
        ans += min_dist
        cnt += 1
        sea[nr][nc] = 0
        return nr, nc
    # 먹을게 없다면 도움 요청 (중단)
    return None

N = int(input())
sea = [list(map(int, input().split())) for _ in range(N)]
ans = 0
dr, dc = (-1,0,1,0), (0,-1,0,1)

shark_weight = 2
cnt = 0
sr, sc = searching_shark()
sea[sr][sc] = 0

while True:

    next_pos = moving(sr, sc)

    if not next_pos:
        break
    sr, sc = next_pos

    if cnt == shark_weight:
        cnt = 0
        shark_weight += 1

print(ans)