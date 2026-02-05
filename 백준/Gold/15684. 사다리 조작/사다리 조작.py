import sys
input = sys.stdin.readline

def recur(cnt, mx):
    global end, ans

    if end:
        return

    if cnt == mx:
        if simul():
            end = True
            ans = mx
        return

    for c in range(1, N):
        for r in range(1, H + 1):
            if ladder[c][r] or ladder[c + 1][r]:
                continue
            ladder[c][r], ladder[c + 1][r] = c + 1, c
            recur(cnt + 1, mx)
            ladder[c][r], ladder[c + 1][r] = 0, 0

def simul():
    for s in range(1, N + 1):
        # print(f'시작은 {s}번')
        cur, r = s, 1
        while r <= H:
            if ladder[cur][r]:
                cur = ladder[cur][r]
            r += 1
        # print(f'끝은 {cur}번')
        # print()
        if cur != s:
            return 0
    return 1

N, M, H = map(int, input().split())
ladder = [[0] * (H + 1) for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    ladder[b][a], ladder[b + 1][a] = b + 1, b

end, ans = False, -1
# print('원본', ladder)
for t in range(0, 4):
    if end:
        break
    recur(0, t)
print(ans)