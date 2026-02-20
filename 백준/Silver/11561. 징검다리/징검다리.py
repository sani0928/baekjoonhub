import math
t = int(input())
nums = list(int(input()) for _ in range(t))
print('\n'.join(str((-1 + math.isqrt(8*n + 1)) // 2) for n in nums))