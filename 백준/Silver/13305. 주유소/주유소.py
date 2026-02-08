import sys
input = sys.stdin.readline
N = int(input())
dist = list(map(int, input().split()))
city = list(map(int, input().split()))
ans = 0
mn_cost = 10 ** 9
for i in range(N - 1):
    if mn_cost > city[i]:
        mn_cost = city[i]
    ans += mn_cost * dist[i]
print(ans)