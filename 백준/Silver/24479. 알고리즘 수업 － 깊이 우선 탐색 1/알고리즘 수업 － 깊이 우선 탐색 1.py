import sys; sys.setrecursionlimit(10**6)

input = sys.stdin.readline
N, M, R = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for chunk in graph:
    chunk.sort()

vis = [0] * (N + 1)
vis[R] = 1
ans = [0] * (N + 1)
ans[R] = 1; step = 2

def dfs(next_pos):
    global step

    for each in graph[next_pos]:
        if not vis[each]:
            vis[each] = 1
            ans[each] = step
            step += 1
            dfs(each)
    return

dfs(R)
print('\n'.join(map(str, ans[1:])))