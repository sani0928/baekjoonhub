def recur(idx, s):
    if idx == n:
        if eval(s.replace(' ', '')) == 0:
            print(s)
        return
    recur(idx + 1, s + ' ' + str(nums[idx]))
    recur(idx + 1, s + '+' + str(nums[idx]))
    recur(idx + 1, s + '-' + str(nums[idx]))

t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(range(1, n + 1))
    recur(1, '1')
    print()