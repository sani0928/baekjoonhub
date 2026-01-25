import sys; from collections import deque
input = sys.stdin.readline

def search(node, again):
    global mx_dist

    q = deque([(0, node)])
    vis = [0] * (n + 1)
    vis[node] = 1
    last_node = None
    while q:
        dist, cur = q.popleft()
        if mx_dist < dist:
            mx_dist, last_node = dist, cur

        for nd, nx in tree[cur]:
            if vis[nx]:
                continue
            vis[nx] = 1
            q.append((dist + nd, nx))

    if again:
        return search(last_node, False)

n = int(input())
if n == 1:
    print(0)
else:
    tree = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v, w = map(int, input().split())
        tree[u].append((w, v))
        tree[v].append((w, u))
    mx_dist = 0
    search(1, True)
    print(mx_dist)