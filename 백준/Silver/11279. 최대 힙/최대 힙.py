import sys; import heapq

input = sys.stdin.readline
N = int(input())
pq = []
for _ in range(N):
    x = int(input())
    if x != 0:
        heapq.heappush(pq, -x)
    else:
        if pq:
            print(-heapq.heappop(pq))
        else:
            print(0)