from itertools import combinations

def select(arr):
    res = 0
    for nums in combinations(arr, 3):
        res = max(res, sum(nums) % 10)
    return res

N = int(input())
highest = 0
winner = -1
for num in range(1, N + 1):
    card = list(map(int, input().split()))
    result = select(card)
    if highest <= result:
        highest = result
        winner = num
print(winner)