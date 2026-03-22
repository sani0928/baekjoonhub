n, d = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
max_h = arr[0]
cnt = 0
if max_h >= d:
    for i in range(n):
        if max_h - arr[i] < d:
            cnt += arr[i] + d - max_h
        else:
            break
    print(cnt)
else:
    print(sum(arr))