import math
num = map(int, input().rstrip())
rec = [0] * 9
for n in num:
    if n == 6 or n == 9:
        rec[6] += 0.5
        continue
    rec[n] += 1
print(math.ceil(max(rec)))