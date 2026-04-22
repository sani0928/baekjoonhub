from collections import deque

s = int(input())
vis = [[-1] * (s*2) for _ in range(s*2)]
vis[1][0] = 0
q = deque([(1, 0)])
while q:
    cur, save = q.popleft()
    if cur == s:
        print(vis[cur][save])
        break
    time = vis[cur][save]
    # 복사
    if vis[cur][cur] == -1:
        vis[cur][cur] = time + 1
        q.append((cur, cur))
    # 붙여넣기
    nx = cur + save
    if save > 0 and nx < s*2 and vis[nx][save] == -1:
        vis[nx][save] = time + 1
        q.append((nx, save))
    # 삭제
    nx = cur - 1
    if nx >= 0 and vis[nx][save] == -1:
        vis[nx][save] = time + 1
        q.append((nx, save))