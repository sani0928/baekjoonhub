N, K = map(int, input().split())
arr = [num for num in range(1, N + 1)]
ans = []
p = 0

for _ in range(N):
    p += K - 1
    if p >= len(arr):
        p %= len(arr)
    ans.append(str(arr.pop(p)))
print('<',", ".join(ans),'>', sep='')