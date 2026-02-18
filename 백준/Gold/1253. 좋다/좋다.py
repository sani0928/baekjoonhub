n = int(input())
arr = list(map(int, input().split()))
arr.sort()
ans = 0
for i in range(n):
    l, r = 0, n - 1
    while l < r:
        if l == i:
            l += 1
            continue
        if r == i:
            r -= 1
            continue
        if arr[l] + arr[r] == arr[i]:
            ans += 1
            break
        if arr[l] + arr[r] > arr[i]:
            r -= 1
        else:
            l += 1
print(ans)