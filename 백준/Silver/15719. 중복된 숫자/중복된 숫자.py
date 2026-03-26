import sys
n = int(sys.stdin.readline())
total = temp = 0
while True:
    chunk = sys.stdin.read(8192)
    if not chunk:
        break
    for num in chunk:
        if num == ' ' or num == '\n':
            total += temp
            temp = 0
        else:
            temp = temp * 10 + (ord(num) - 48)
total += temp
print(total - (n * (n - 1) // 2))