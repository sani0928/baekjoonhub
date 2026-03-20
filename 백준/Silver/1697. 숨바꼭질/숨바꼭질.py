import heapq

pos, target = map(int, input().split())

pq = []
heapq.heappush(pq, (0, pos))
ans = float('inf')

visited = [[False] * 3 for _ in range(100001)]
for i in range(3):
    visited[pos][i] = True
while pq:

    cnt, pos = heapq.heappop(pq)

    if cnt > ans:
        break

    if pos == target and cnt <= ans:
        ans = cnt


    if 0 <= pos - 1 <= 100000 and not visited[pos - 1][0]:
        visited[pos - 1][0] = True
        heapq.heappush(pq, (cnt + 1, pos - 1))
    if 0 <= pos + 1 <= 100000 and not visited[pos + 1][1]:
        visited[pos + 1][1] = True
        heapq.heappush(pq, (cnt + 1, pos + 1))
    if 0 <= pos * 2 <= 100000 and not visited[pos * 2][2]:
        visited[pos * 2][2] = True
        heapq.heappush(pq, (cnt + 1, pos * 2))

print(ans)
