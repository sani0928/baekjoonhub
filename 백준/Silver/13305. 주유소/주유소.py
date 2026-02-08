import sys
input = sys.stdin.readline
N = int(input())
dist = list(map(int, input().split()))
city = list(map(int, input().split()))
ans = 0
for i in range(N - 1):
    mn = 10 ** 9
    for j in range(i + 1):
        mn = min(mn, dist[i] * city[j])
    ans += mn
print(ans)