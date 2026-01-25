docu = input()
char = input()
dl, cl = len(docu), len(char)
cnt, cur = 0, 0
while cur <= dl - cl:
    if docu[cur] == char[0]:
        i = 0
        l = cur
        while i < cl and l < dl and docu[l] == char[i]:
            l += 1
            i += 1
        if i == cl:
            cnt += 1
            cur = l
        else:
            cur += 1
        continue
    cur += 1
print(cnt)