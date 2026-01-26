import sys
input = sys.stdin.readline

n = int(input())
line = sorted([int(input()) for _ in range(n)], reverse=True)
order, ans = 0, 0
i = 0
while i < n and line[i] - order > 0:
    ans += line[i] - order
    order += 1
    i += 1
print(ans)