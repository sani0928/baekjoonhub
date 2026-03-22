def calcul():
    cnt, i = 0, 0
    while i < n and max_h - arr[i] < d:
        cnt += arr[i] + d - max_h
        i += 1
    return cnt

n, d = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
max_h = arr[0]
print(calcul() if max_h >= d else sum(arr))