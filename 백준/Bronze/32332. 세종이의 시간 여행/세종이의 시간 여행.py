def calcul_days(y, m, d):
    return y*360 + ((m-1)*30) + (d-1)

def to_calender(days):
    y = days // 360; days %= 360
    m = days // 30 + 1; days %= 30
    d = days % 30 + 1
    return int(y), int(m), int(d)

y0, m0, d0, w0, g0 = map(float, input().split())
y1, m1, d1, w1, g1 = map(float, input().split())
ans = [0] * 5
ans[3], ans[4] = w0, g0
cur = calcul_days(y0, m0, d0)
arr = 2*cur - calcul_days(y1, m1, d1)
ans[0], ans[1], ans[2] = to_calender(arr)
diff_w, diff_g = abs(w0 - w1), abs(g0 - g1)
if w0 > w1:
    ans[3] += diff_w
else:
    ans[3] -= diff_w
if g0 > g1:
    ans[4] += diff_g
else:
    ans[4] -= diff_g
print(ans[0], ans[1], ans[2], format(ans[3], '.3f'), format(ans[4], '.3f'))