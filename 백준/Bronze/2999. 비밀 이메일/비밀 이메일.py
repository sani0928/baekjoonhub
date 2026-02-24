msg = input()
n = len(msg)
r = 1
v = 1
while v * v <= n:
    if n % v == 0:
        r = v
    v += 1
print(''.join(msg[j] for i in range(r) for j in range(i, len(msg), r)))