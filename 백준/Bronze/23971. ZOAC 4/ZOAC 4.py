def calcul(l, d):
    if l - 1 >= d + 1:
        return (l - 1) // (d + 1) + 1
    return 0

h, w, n, m = map(int, input().split())
h_cnt, w_cnt = calcul(h, n), calcul(w, m)
if w_cnt == 0 or h_cnt == 0:
    if w_cnt == 0 and h_cnt != 0: print(h_cnt)
    elif w_cnt != 0 and h_cnt == 0: print(w_cnt)
    else: print(1)
else: print(h_cnt * w_cnt)