import sys; from collections import deque
input = sys.stdin.readline

def go(x):
    cnt = 0
    q = deque([x])
    v = [0] * (n + 1)
    v[x] = 1
    while q:
        cur = q.popleft()
        for nx in prev[cur]:
            if not v[nx]:
                cnt += 1
                v[nx] = 1
                q.append(nx)
    return cnt

n, m = map(int, input().split())
prev = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    prev[b].append(a)
start = int(input())
print(go(start))