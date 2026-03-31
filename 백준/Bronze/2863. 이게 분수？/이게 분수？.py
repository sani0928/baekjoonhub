arr = [tuple(map(int, input().split())) for _ in range(2)]
ans = mx = i = 0
while i < 4:
    value = (arr[0][0] / arr[1][0]) + (arr[0][1] / arr[1][1])
    if mx < value:
        mx = value
        ans = i
    arr = list(zip(*arr[::-1]))
    i += 1
print(ans)