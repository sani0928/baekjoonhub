from collections import deque

F, S, G, U, D = map(int, input().split())
vis = [0] * (F + 1)
vis[S] = 1
q = deque([(S, 0)])
ans = 'use the stairs'

while q:

    pos, cnt = q.popleft()
    if pos == G:
        ans = cnt
        break

    for go in [U, -D]:
        next_pos = pos + go
        if 0 < next_pos <= F and not vis[next_pos]:
            vis[next_pos] = 1
            q.append((next_pos, cnt + 1))
print(ans)