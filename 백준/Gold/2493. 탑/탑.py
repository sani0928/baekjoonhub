n = int(input())
arr = [0] + list(map(int, input().split()))
ans = [0] * (n + 1)
s = [(arr[1], 1)]
for i in range(2, n + 1):
    if s[-1][0] < arr[i]:
        while s and s[-1][0] < arr[i]:
            s.pop()
        if not s:
            ans[i] = 0
        else:
            ans[i] = s[-1][1]
    else:
        ans[i] = s[-1][1]
    s.append((arr[i], i))
print(*ans[1:])