from collections import deque

K = int(input())
W, H = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(H)]
dist = [[[-1] * (K + 1) for _ in range(W)] for _ in range(H)]

dr, dc = (0,1,0,-1), (1,0,-1,0)
hr, hc = (1,2,2,1,-1,-2,-2,-1), (2,1,-1,-2,-2,-1,1,2)

# 0,0,K 일 때는 최단거리 0
dist[0][0][K] = 0
# 시작위치(r,c) / 말움직임 가능 횟수
q = deque([(0,0,K)])

def go():

    while q:

        r, c, horse_moving = q.popleft()
        # 현 상태에서의 최단거리
        d = dist[r][c][horse_moving]

        if r == H- 1 and c == W - 1:
            return d

        # 일반 4방향
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < H and 0 <= nc < W and grid[nr][nc] != 1 and dist[nr][nc][horse_moving] == -1:
                dist[nr][nc][horse_moving] = d + 1
                q.append((nr, nc, horse_moving))

        # 말 동작 8방향
        if horse_moving != 0:
            for k2 in range(8):
                hnr, hnc = r + hr[k2], c + hc[k2]
                if 0 <= hnr < H and 0 <= hnc < W and grid[hnr][hnc] != 1 and dist[hnr][hnc][horse_moving - 1] == -1:
                    dist[hnr][hnc][horse_moving - 1] = d + 1
                    q.append((hnr, hnc, horse_moving - 1))

    return -1

print(go())