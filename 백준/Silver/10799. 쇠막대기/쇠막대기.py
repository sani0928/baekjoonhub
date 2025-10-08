bong = list(map(str, input().strip()))

cnt = 0
ans = 0

for i in range(len(bong)):
    if bong[i] == '(':
        cnt += 1
    else:
        # 레이저면
        if bong[i-1] == '(':
            # cnt 취소하고 잘린 갯수 추가
            cnt -= 1
            ans += cnt
        # 레이저가 아니면
        else:
            # cnt 하나 없애고 잘린 갯수 1개 추가
            cnt -= 1
            ans += 1

print(ans)