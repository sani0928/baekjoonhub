import sys, heapq

input = sys.stdin.readline
N = int(input())

q = []

for _ in range(N):
    num = int(input())
    if num > 0:
        heapq.heappush(q, (num, num))
    elif num < 0:
        heapq.heappush(q, (-num, num))
    else:
        if q:
            ans = heapq.heappop(q)[1]
            print(ans)
        else:
            print(0)