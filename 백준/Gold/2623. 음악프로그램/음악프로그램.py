import sys
from collections import deque
input = sys.stdin.readline

def solve():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    indegree = [0] * (N + 1)
    for _ in range(M):
        cnt, *rank = map(int, input().split())
        for i in range(1, cnt):
            indegree[rank[i]] += i
            for j in range(i):
                graph[rank[j]].append(rank[i])
    ans = []
    q = deque()
    for i in range(1, N + 1):
        if indegree[i] != 0:
           continue
        ans.append(i)
        q.append(i)

    while q:
        cur = q.popleft()
        for nx in graph[cur]:
            indegree[nx] -= 1
            if indegree[nx] == 0:
                ans.append(nx)
                q.append(nx)
                
    if len(ans) == N:
        for node in ans:
            print(node)
    else:
        print(0)

if __name__ == '__main__':
    solve()