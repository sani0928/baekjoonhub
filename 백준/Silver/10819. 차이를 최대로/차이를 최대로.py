from itertools import permutations

def calculator(lst):
    total = 0
    for i in range(N-1):
        total += abs(lst[i] - lst[i+1])
    return total

N = int(input())
nums = list(map(int, input().split()))
max_sum = 0

for num in permutations(nums, N):
    max_sum = max(max_sum, calculator(num))

print(max_sum)