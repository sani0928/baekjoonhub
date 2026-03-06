rec = [0] * 26
for c in input():
    rec[ord(c) - 97] += 1
print(*rec)