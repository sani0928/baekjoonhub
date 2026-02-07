N = int(input())
M = int(input())
S = list(input().strip())
pl = 2 * N + 1
ans = 0
cnt = 0
cur = 'O'
for i in range(M):
    if cur == 'I':
        if S[i] == 'O':
            cnt += 1
        else:
            cnt = 1
    else: # cur == 'O'
        if S[i] == 'I':
            cnt += 1
        else:
            cnt = 0
    if cnt == pl:
        ans += 1
        cnt -= 2
    cur = S[i]

print(ans)