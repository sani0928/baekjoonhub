from heapq import heappush, heappop

s = int(input())
vis = [[-1] * (s*2) for _ in range(s*2)]
vis[1][0] = 0
hq = []
heappush(hq, (vis[1][0], 1, 0))
while hq:
    time, cur, save = heappop(hq)
    if cur == s:
        print(vis[cur][save])
        break
    # 복사
    if vis[cur][cur] == -1:
        vis[cur][cur] = time + 1
        heappush(hq, (vis[cur][cur], cur, cur))
    # 붙여넣기
    nx = cur + save
    if save > 0 and nx < s*2 and vis[nx][save] == -1:
        vis[nx][save] = time + 1
        heappush(hq, (vis[nx][save], nx, save))
    # 삭제
    nx = cur - 1
    if vis[nx][save] == -1:
        vis[nx][save] = time + 1
        heappush(hq, (vis[nx][save], nx, save))