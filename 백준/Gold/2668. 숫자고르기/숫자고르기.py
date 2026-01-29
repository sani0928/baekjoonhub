def dfs(start, cur):
    global cnt

    for nx in graph[cur]:
        if nx == start:
            ans.append(start)
            cnt += 1
            return
        if vis[start][nx]:
            continue
        vis[start][nx] = 1
        dfs(start, nx)

n = int(input())
graph = [[] for _ in range(n + 1)]
vis = [[0] * (n + 1) for _ in range(n + 1)]
cnt, ans = 0, []
for i in range(1, n + 1):
    graph[i].append(int(input()))
for snd in range(1, n + 1):
    dfs(snd, snd)
print(cnt)
print(*ans, sep='\n')