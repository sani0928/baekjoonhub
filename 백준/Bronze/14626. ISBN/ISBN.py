MOD = 10
arr = list(map(str, input().rstrip()))
ans = 0
target, w = None, None
for i in range(13):
    if not arr[i].isdigit():
        target = i
        w = 1 if target % 2 == 0 else 3
        continue
    num = int(arr[i])
    if i % 2 == 0:
        ans += num % MOD
    else:
        ans += 3 * num % MOD

for x in range(10):
    if (ans + w * x) % 10 == 0:
        print(x)
        break