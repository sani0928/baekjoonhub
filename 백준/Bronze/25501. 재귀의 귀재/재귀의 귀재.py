def recur(l, r):
    global cnt
    if l >= r:
        return 1
    if s[l] != s[r]:
        return 0
    cnt += 1
    return recur(l + 1, r - 1)

t = int(input())
while t != 0:
    s = input()
    cnt = 1
    print(recur(0, len(s) - 1), cnt)
    t -= 1