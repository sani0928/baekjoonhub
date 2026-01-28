x, y = {}, {}
ans, ans2 = 0, 0
for _ in range(3):
    a, b = map(int, input().split())
    if x.get(a):
        x[a] += 1
    else:
        x[a] = 1
    if y.get(b):
        y[b] += 1
    else:
        y[b] = 1
for k in x.keys():
    if x[k] == 1:
        ans = k
        break
for k in y.keys():
    if y[k] == 1:
        ans2 = k
        break
print(ans, ans2)