n, ct = int(input()), list(map(int, input().split()))
ct.sort()
s = sum(ct)
goal, rest = s // n, s % n
ans = 0
for l in range(n - rest):
    if ct[l] > goal: ans += ct[l] - goal
for r in range(n - rest, n):
    if ct[r] > goal + 1: ans += ct[r] - (goal + 1)
print(ans)