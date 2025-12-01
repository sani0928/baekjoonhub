T = int(input())
for _ in range(T):
    lst = list(map(str, input().strip()))
    s = []; nope = False
    for i in range(len(lst)):
        if lst[i] == '(':
            s.append('(')
        else:
            if not s:
                nope = True
                break
            s.pop()
    if nope or s:
        print('NO')
        continue
    else:
        print('YES')