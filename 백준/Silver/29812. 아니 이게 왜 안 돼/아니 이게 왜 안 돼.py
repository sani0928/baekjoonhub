def drag(start):
    l = 1
    for j in range(start + 1, n):
        if s[j] in "HYU":
            return l
        l += 1
    return l

rec = {'H': 0, 'Y': 0, 'U': 0}
n = int(input())
s = input().rstrip()
d, m = map(int, input().split())
ans = 0
i = 0
while i < n:
    if s[i] in "HYU":
        rec[s[i]] += 1
        i += 1
        continue
    t = drag(i)
    ans += min(d+m, d*t)
    i += t

cnt = min(rec.values())
print(ans if ans > 0 else 'Nalmeok')
print(cnt if cnt > 0 else 'I love HanYang University')