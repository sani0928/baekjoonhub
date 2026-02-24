import sys; from collections import defaultdict
input = sys.stdin.readline

def is_fast(pos):
    for idx in range(pos):
        if not check[idx]:
            return False
    return True

n = int(input())
memo = defaultdict(int)
for r in range(n):
    memo[input().rstrip()] = r
ans = 0
order = 1
check = [0] * n
for _ in range(n):
    car = input().rstrip()
    if not is_fast(memo[car]):
        ans += 1
    check[memo[car]] = 1
print(ans)