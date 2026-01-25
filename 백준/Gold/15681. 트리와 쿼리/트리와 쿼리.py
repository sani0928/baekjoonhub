import sys; sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def maketree(root):
    t = [[] for _ in range(n + 1)]
    s = [root]
    vis = [0] * (n + 1)
    vis[root] = 1
    while s:
        cur = s.pop()
        for nx in graph[cur]:
            if vis[nx]:
                continue
            vis[nx] = 1
            t[cur].append(nx)
            s.append(nx)
    return t

def cal_cnt(cur, cnt):

    if not tree[cur]:
        sub_tree_cnt[cur] = 1
        return sub_tree_cnt[cur]

    for nx in tree[cur]:
        cnt += cal_cnt(nx, 1)

    sub_tree_cnt[cur] = cnt
    return sub_tree_cnt[cur]


n, r, q = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
tree = maketree(r)
sub_tree_cnt = [0] * (n + 1)
cal_cnt(r, 1)
for _ in range(q):
    print(sub_tree_cnt[int(input())])