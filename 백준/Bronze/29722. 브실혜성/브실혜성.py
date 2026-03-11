def calcul(rest, mod):
    return rest // mod, rest % mod

d = list(map(int, input().split('-')))
to_day = (d[0] * 360) + ((d[1] - 1) * 30) + (d[2] - 1)
to_day += int(input())
d[0], to_day = calcul(to_day, 360)
d[1], to_day = calcul(to_day, 30)
d[2] = to_day
d[1], d[2] = d[1] + 1, d[2] + 1
print(f'{d[0]:04d}-{d[1]:02d}-{d[2]:02d}')