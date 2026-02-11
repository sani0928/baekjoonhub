import sys; sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(cur):
    cnt = 1
    for nx in tree[cur]:
        if parent[cur] == nx:
            continue
        parent[nx] = cur
        cnt += dfs(nx)
    sub_cnt[cur] = cnt
    return sub_cnt[cur]

N, R, Q = map(int, input().split())
tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)
sub_cnt = [1] * (N + 1)
parent = [-1] * (N + 1)
parent[R] = 0
dfs(R)
print(*(sub_cnt[int(input())] for _ in range(Q)), sep='\n')