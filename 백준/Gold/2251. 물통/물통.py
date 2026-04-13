seen, ans = set(), set()
mx = tuple(map(int, input().split()))
s= [[0, 0, mx[2]]]
while s:
    cur = s.pop()
    if tuple(cur) in seen:
        continue
    seen.add(tuple(cur))
    if cur[0] == 0:
        ans.add(cur[2])
        
    for i in range(3):
        for j in range(3):
            if i == j or cur[i] == 0 or cur[j] == mx[j]:
                continue
            nx = cur.copy()
            mn = min(nx[i], mx[j] - nx[j])
            nx[i] -= mn
            nx[j] += mn
            s.append(nx)

print(*sorted(ans))