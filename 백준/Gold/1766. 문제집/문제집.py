import heapq

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)
ans = []
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    indegree[v] += 1

hq = []
for i in range(1, N + 1):
    if indegree[i] == 0:
        heapq.heappush(hq, i)
cnt = 0
while hq:
    exam = heapq.heappop(hq)
    ans.append(exam)

    for after in graph[exam]:
        indegree[after] -= 1
        if indegree[after] == 0:
            heapq.heappush(hq, after)

print(*ans)