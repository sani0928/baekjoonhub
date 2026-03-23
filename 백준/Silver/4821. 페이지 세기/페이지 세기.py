while True:
    n = int(input())
    if n == 0:
        break
    cnt = 0
    page = [0] * (n + 1)
    R = list(input().split(','))
    for r in R:
        if r.isdigit():
            l = h = int(r)
        else:
            l, h = map(int, r.split('-'))

        if l > h:
            continue
        for i in range(l, h + 1):
            if 0 > i or i > n:
                break
            if not page[i]:
                cnt += 1
                page[i] = 1
    print(cnt)