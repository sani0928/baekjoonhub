n, m = map(int, input().split())
s = list(map(int, input().rstrip()))
i = 0
while i < len(s) and m > 0:
    if s[i] != 0:
        diff = 9 - s[i] + 1
        if m >= diff:
            m -= diff
            s[i] = 0
    i += 1
if m > 0:
    s[-1] = (s[-1] + m % 10) % 10
print(*s, sep='')