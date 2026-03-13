n = int(input())
total = 0
while n > 0:
    if n >= 5 and n % 5 == 0:
        total += n // 5
        n = 0
    else:
        total += 1
        n -= 3
print(total if n == 0 else -1)