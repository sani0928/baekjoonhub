from datetime import datetime

N, L, F = input().split()
N, F = int(N), int(F)
# 분 기준
limit = int(L[:3]) * 1440 + int(L[4:6]) * 60 + int(L[7:9])

flist, note = {}, {}
for _ in range(N):
    date, t, item, nick = input().split()
    month, day = int(date.split('-')[1]), int(date.split('-')[2])
    hour, minute = int(t.split(':')[0]), int(t.split(':')[1])
    now = datetime(2021, month, day, hour, minute)
    # 대여하러 옴
    if not note.get((nick, item)):
        note[(nick, item)] = now
        continue

    before = note[(nick, item)]
    total = ((now - before).days * 1440) + ((now - before).seconds // 60)
    # 늦어서 벌금
    diff = total - limit
    if diff > 0:
        if flist.get(nick):
            flist[nick] += diff * F
            continue
        flist[nick] = diff * F
    del note[(nick, item)]

if flist:
    for k in sorted(flist):
        print(k, flist[k])
else:
    print(-1)