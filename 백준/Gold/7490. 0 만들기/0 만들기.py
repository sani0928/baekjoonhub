def calcul(s):
    res = 0
    opt = 1 # +는 1, -는 -1
    i = 0
    while i < len(s):
        if s[i] == '+':
            opt = 1
        elif s[i] == '-':
            opt = -1
        else:
            num = 0
            while i < len(s) and (s[i].isdigit() or s[i] == ' '):
                if s[i].isdigit():
                    num = num * 10 + int(s[i])
                i += 1
            res += opt * num
            continue
        i += 1
    return res == 0

def recur(idx, s):
    if idx == n:
        if calcul(s):
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