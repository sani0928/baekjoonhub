import heapq

N, M = map(int, input().split())
vis = [0] * 101
ladder = [0] * 101
snake = [0] * 101
for _ in range(N):
    u, v = map(int,input().split())
    ladder[u] = v
for _ in range(M):
    u, v = map(int,input().split())
    snake[u] = v
hq = []
heapq.heappush(hq, (0, 1, [1]))
while hq:
    cnt, cur, footprint = heapq.heappop(hq)
    if cur == 100:
        print(cnt)
        break

    for i in range(1, 7):
        nx = cur + i
        if nx <= 100 and not vis[nx]:
            vis[nx] = 1
            if ladder[nx]:
                heapq.heappush(hq, (cnt + 1, ladder[nx], footprint + [ladder[nx]]))

            elif snake[nx]:
                heapq.heappush(hq, (cnt + 1, snake[nx], footprint + [snake[nx]]))
            else:
                heapq.heappush(hq, (cnt + 1, nx, footprint + [nx]))