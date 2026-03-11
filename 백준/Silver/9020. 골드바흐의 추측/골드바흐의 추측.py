import sys
input = sys.stdin.readline

def check(num):
    for x in range(2, num):
        if num % x == 0:
            return 0
    return 1

t = int(input())
nums = [int(input()) for _ in range(t)]
prime = [0] * (max(nums) + 1)
prime[0] = prime[1] = 1
for i in range(2, max(nums) + 1):
    if check(i):
        prime[i] = 1
for n in nums:
    mid = n // 2
    if prime[mid]:
        print(mid, mid)
        continue
    diff = 1
    while not (prime[mid - diff] and prime[mid + diff]):
        diff += 1
    print(mid - diff, mid + diff)