while True:
    n = int(input())
    if not n:
        break
    s = input().replace(' ', '').upper()
    l = len(s)
    ans = [''] * l
    p = 0
    for i in range(n):
        for j in range(i, l, n):
            ans[j] = s[p]
            p += 1
    print(''.join(ans))