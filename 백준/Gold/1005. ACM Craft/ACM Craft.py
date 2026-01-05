import sys, heapq
input = sys.stdin.readline

T = int(input())
def solution():
    N, K = map(int, input().split())
    time = [0] + list(map(int, input().split()))
    graph = [[] for _ in range(N + 1)]
    indegree = [0] * (N + 1)
    for _ in range(K):
        u, v  = map(int, input().split())
        graph[u].append(v)
        indegree[v] += 1
    target = int(input())

    hq = []
    for i in range(1, N + 1):
        if not indegree[i]:
            heapq.heappush(hq, (time[i], i))
    while hq:
        total_time, pos = heapq.heappop(hq)
        if pos == target:
            print(total_time)
            break
            
        for nx in graph[pos]:
            indegree[nx] -= 1
            if indegree[nx] == 0:
                heapq.heappush(hq, (total_time + time[nx], nx))
    return

if __name__ == "__main__":
    for _ in range(T):
        solution()