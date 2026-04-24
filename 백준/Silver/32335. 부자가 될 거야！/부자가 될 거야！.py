n, m = map(int, input().split())
s = list(map(int, input().rstrip()))
for i in range(len(s)):
    if s[i] == 0:
        continue
    diff = 9 - s[i] + 1
    if m >= diff:
        m -= diff
        s[i] = 0
    if m == 0:
        break
s[-1] = (s[-1] + m % 10) % 10
print(*s, sep='')