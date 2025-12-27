import sys
input = sys.stdin.readline

def hacking(start):
    global max_cnt

    cnt = 0
    vis = [0] * (N + 1)
    vis[start] = 1
    s = [start]

    while s:

        cur = s.pop()

        for each in graph[cur]:
            if not vis[each]:
                vis[each] = 1
                cnt += 1
                s.append(each)

    max_cnt = max(max_cnt, cnt)
    return cnt

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
max_cnt = 0
for _ in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)

ans = [0] * (N + 1)
for computer in range(1, N + 1):
    ans[computer] = hacking(computer)

print(*[i for i in range(1, N + 1) if ans[i] == max_cnt])