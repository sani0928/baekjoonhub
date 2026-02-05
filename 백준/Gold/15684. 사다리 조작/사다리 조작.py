import sys
input = sys.stdin.readline

def recur(cnt, mx):
    global ans

    if ans <= mx:
        return

    if cnt == mx:
        if simul():
            ans = mx
        return

    for c in range(1, N):
        # 독립적인 세로선은 제외
        if c in alone:
            continue
        for r in range(1, H + 1):
            if ladder[c][r] or ladder[c + 1][r]:
                continue
            ladder[c][r], ladder[c + 1][r] = c + 1, c
            recur(cnt + 1, mx)
            ladder[c][r], ladder[c + 1][r] = 0, 0

def simul():
    for s in range(1, N + 1):
        cur, r = s, 1
        while r <= H:
            if ladder[cur][r]:
                cur = ladder[cur][r]
            r += 1
        # 시작과 끝이 다르면 실패
        if cur != s:
            return 0
    return 1

def check_alone(l):
    for j in ladder[l]:
        if j != 0:
            return 0
    return 1

N, M, H = map(int, input().split())
ladder = [[0] * (H + 1) for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    ladder[b][a], ladder[b + 1][a] = b + 1, b

alone = set()
for i in range(1, N + 1):
    if check_alone(i):
        alone.add(i)

ans = 4
for t in range(0, 4):
    recur(0, t)

if ans < 4:
  print(ans)
else:
  print(-1)