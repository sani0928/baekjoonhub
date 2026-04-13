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
            mn = min(nx[i], mx[j] - nx[j])
            nx[i] -= mn
            nx[j] += mn
            back(nx)

seen = set()
ans = set()
mx = tuple(map(int, input().split()))
back([0, 0, mx[2]])
print(*sorted(ans))