import sys
input = sys.stdin.readline

ans = 0
n = int(input())
arr = list(tuple(map(int, input().split())) for _ in range(n))
arr.sort()
s, e = arr[0]
for i in range(1, n):
    l, r = arr[i]
    if l > e:
        ans += e - s
        s, e = l, r
    else:
        if r > e:
            e = r
ans += e - s
print(ans)