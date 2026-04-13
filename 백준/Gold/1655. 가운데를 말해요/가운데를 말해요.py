import sys, heapq
input = sys.stdin.readline

n = int(input())
l, r = [], []
for _ in range(n):
    num = int(input())
    if len(l) == len(r):
        heapq.heappush(l, -num)
    else:
        heapq.heappush(r, num)
    if r and -l[0] > r[0]:
        mx_l = -heapq.heappop(l)
        mn_r = heapq.heappop(r)
        heapq.heappush(l, -mn_r)
        heapq.heappush(r, mx_l)
    print(-l[0])