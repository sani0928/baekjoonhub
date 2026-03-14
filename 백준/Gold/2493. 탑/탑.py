n = int(input())
arr = list(map(int, input().split()))
ans = [0] * n
s = [(arr[0], 0)]
for i in range(1, n):
    while s and s[-1][0] < arr[i]:
        s.pop()
    if not s:
        ans[i] = 0
    else:
        ans[i] = s[-1][1] + 1
    s.append((arr[i], i))
print(*ans)