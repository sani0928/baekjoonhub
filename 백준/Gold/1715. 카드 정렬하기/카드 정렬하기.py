import sys, heapq
input = sys.stdin.readline

n = int(input())
if n == 1:
    print(0)
    sys.exit(0)
hq = []
for _ in range(n):
    heapq.heappush(hq, int(input()))
ans = 0
while hq:
    a, b = heapq.heappop(hq), heapq.heappop(hq)
    ans += (a + b)
    if hq:
        heapq.heappush(hq, a + b)
print(ans)