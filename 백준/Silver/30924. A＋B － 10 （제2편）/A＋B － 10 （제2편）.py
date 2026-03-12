import random

arr = [n for n in range(1, 10001)]
random.shuffle(arr)
A, B = 0, 0
for n in arr:
    print("? A", n, flush=True)
    res = int(input())
    if res == 1:
        A = n
        break
for n in arr:
    print("? B", n, flush=True)
    res = int(input())
    if res == 1:
        B = n
        break

print(f'! {A + B}')