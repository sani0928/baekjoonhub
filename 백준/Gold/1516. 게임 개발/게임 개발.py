from collections import deque; import sys; input = sys.stdin.readline

n = int(input())
in_degree = [0] * (n + 1)
dp = [0] * (n + 1)
time = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
q = deque()
for i in range(1, n + 1):
    info = list(map(int, input().split()))
    time[i] = info[0]
    if len(info) > 2: # 상위 루트 존재
        for j in info[1:-1]:
            graph[j].append(i)
            in_degree[i] += 1
    else: # 상위 루트 존재 X
        dp[i] = time[i]
        q.append(i)

while q:
    cur = q.popleft()
    for nx in graph[cur]:
        # 더 오래 걸리는 경우가 생기면 갱신
        dp[nx] = max(dp[nx], dp[cur] + time[nx])
        in_degree[nx] -= 1
        # 모든 상위 루트 탐색이 끝나면 하위 루트 진행
        if in_degree[nx] == 0:
            q.append(nx)
for i in range(1, n + 1):
    print(dp[i])