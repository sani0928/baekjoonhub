n = int(input())
arr = list(map(int, input().split()))
mx_len, cnt = 0, 0
ans = 0
for i in range(n):
    if mx_len < arr[i]:
        mx_len = arr[i]
        ans = max(ans, cnt)
        cnt = 0
        continue
    cnt += 1
ans = max(ans, cnt)
print(ans)