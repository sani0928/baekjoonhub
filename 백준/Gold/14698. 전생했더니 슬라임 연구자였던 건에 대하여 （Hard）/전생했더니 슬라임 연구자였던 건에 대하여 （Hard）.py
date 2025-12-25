import sys, heapq

input = sys.stdin.readline
mod = 1000000007
t = int(input())
for _ in range(t):

    N = int(input())
    if N == 1:
        input()
        print(1)
        continue

    slims = list(map(int, input().split()))
    heapq.heapify(slims)
    cost = 1

    while len(slims) > 1:

        slim1 = heapq.heappop(slims)
        slim2 = heapq.heappop(slims)
        new_slim = slim1 * slim2
        cost = (cost * new_slim) % mod
        heapq.heappush(slims, new_slim)

    print(cost)