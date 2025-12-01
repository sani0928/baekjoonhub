import sys
from collections import defaultdict
input = sys.stdin.readline
N = int(input())
nums = []
for _ in range(N):
    nums.append(int(input()))
nums.sort()
cnt = defaultdict(int)
for num in nums:
    cnt[num] += 1
max_freq = max(cnt.values())
candidate = [n for n in cnt if cnt[n] == max_freq]
print(round(sum(nums) / N))
print(nums[N//2])
if len(candidate) == 1:
    print(candidate[0])
else:
    print(candidate[1])
print(nums[-1] - nums[0])