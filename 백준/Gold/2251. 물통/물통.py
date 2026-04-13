def back(cur):
    if tuple(cur) in seen:
        return
    seen.add(tuple(cur))
    if cur[0] == 0:
        ans.add(cur[2])

    # i = 물을 주는 위치, j = 물을 받는 위치
    for i in range(3):
        for j in range(3):
            if i == j or cur[i] == 0 or cur[j] == mx[j]:
                continue
            nx = cur.copy()
            total = nx[j] + nx[i]
            # 물을 모두 줘도 남거나 딱 꽉 찰 경우
            if total <= mx[j]:
                nx[i] = 0
                nx[j] = total
            # 물을 모두 주면 넘치는 경우
            else:
                nx[i] = nx[i] - (mx[j] - nx[j])
                nx[j] = mx[j]
            back(nx)

seen = set()
ans = set()
mx = tuple(map(int, input().split()))
back([0, 0, mx[2]])
print(*sorted(ans))