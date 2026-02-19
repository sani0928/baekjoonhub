import sys
input = sys.stdin.readline
s1, s2 = input().rstrip(), input().rstrip()
if len(s1) > len(s2):
    lg, sht = s1, s2
else:
    lg, sht = s2, s1
rec = [0] * (len(sht) + 1)
mx = 0
for ch in lg:
    keep = 0
    for i in range(1, len(sht) + 1):
        last = rec[i]
        if ch == sht[i - 1]:
            rec[i] = keep + 1
            mx = max(mx, rec[i])
        else:
            rec[i] = 0
        keep = last
print(mx)