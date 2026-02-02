import sys
from datetime import datetime
input = sys.stdin.readline

def check(current, before):
    total = ((current - before).days * 1440) + ((current - before).seconds // 60)
    diff = total - limit
    # 기간 초과
    if diff > 0:
        if flist.get(nick):
            flist[nick] += diff * F
            return
        flist[nick] = diff * F
    del note[(nick, item)]

N, L, F = input().split()
N, F = int(N), int(F)
# 분 기준
l_day, l_time = L.split('/')
l_h, l_m = map(int, l_time.split(':'))
limit = int(l_day) * 1440 + l_h * 60 + l_m

flist, note = {}, {}
for _ in range(N):
    date, time, item, nick = input().split()
    _, month, day = map(int, date.split('-'))
    hour, minute = map(int, time.split(':'))
    now = datetime(2021, month, day, hour, minute)
    # 대여
    if not note.get((nick, item)):
        note[(nick, item)] = now
        continue
    # 반납
    check(now, note[nick, item])

if flist:
    for k in sorted(flist):
        print(k, flist[k])
else:
    print(-1)