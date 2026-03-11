import sys
input = sys.stdin.readline

def check(num):
    for i in range(2, num):
        if num % i == 0:
            return 0
    return 1

t = int(input())
for _ in range(t):
    n = int(input())
    if check(n // 2):
        print(n//2, n//2)
        continue
    mid = n // 2
    diff = 1
    while True:
        if check(mid - diff) and check(mid + diff):
            break
        diff += 1
    print(mid - diff, mid + diff)