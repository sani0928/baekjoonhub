def solve(c, i, ans):
    if not c:
        return ans
    ch = chs[i]
    if c < ch:
        return solve(c, i + 1, ans)
    ans += c // ch
    c %= ch
    return solve(c, i + 1, ans)

n = int(input())
chs = (500, 100, 50, 10, 5, 1)
print(solve(1000 - n, 0, 0))