def making():

    temp = []
    p = 0
    digit = ''
    while p < len(lst):
        if lst[p].isdigit():
            digit += lst[p]
        else:
            temp.append(int(digit))
            digit = ''
            temp.append(lst[p])
        p += 1
        
    temp.append(int(digit))
    return temp

def minium():
    global p2, ans

    minus = 0
    p3 = p2 + 1

    while p3 < len(ex) and ex[p3] != '-':
        if type(ex[p3]) == int:
            minus += ex[p3]
        p3 += 1
        
    ans -= minus
    p2 = p3
    return

lst = input()
ex = making()

ans = 0
p2 = 0
check = False
while p2 < len(ex):

    if type(ex[p2]) == int:
        ans += ex[p2]
    else:
        if ex[p2] == '-':
            check = True
            minium()
    if check:
        check = False
    else:
        p2 += 1

print(ans)


