N = int(input())
ans = 0
for _ in range(N):
    string = list(map(str, input().rstrip()))
    lst = []
    last = string[0]
    lst.append(last)
    i = 1
    while i < len(string):
        if string[i] != last:
            if not string[i] in lst:
                last = string[i]
                lst.append(last)     
            else:
                break
            i += 1
        else:
            i += 1
    if i == len(string):
        ans += 1
print(ans)