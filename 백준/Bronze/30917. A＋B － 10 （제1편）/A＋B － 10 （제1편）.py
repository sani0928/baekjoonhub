A, B = 0, 0

for a in range(1, 10):
    print("? A", a, flush=True)
    res = int(input())
    if res == 1:
        A = a
        break

for b in range(1, 10):
    print("? B", b, flush=True)
    res = int(input())
    if res == 1:
        B = b
        break

print(f'! {A + B}')