N = int(input())
arr = list(map(int, input().split()))
ans = (arr[0], arr[1])
min_value = abs(arr[0] + arr[1])
l, r = 0, N - 1
while l < r:
    value = arr[l] + arr[r]
    if min_value >= abs(value):
        ans = (arr[l], arr[r])
        min_value = abs(value)
    # 음수(알칼리성이)면 값을 키우고, 양수(산성이)면 값을 줄여서 0에 가깝게
    if value < 0:
        l += 1
    elif value > 0:
        r -= 1
    # 0이면 즉시 종료
    else:
        break
print(*ans)