N, L = map(int, input().split())
DNA = input()
a, c, g, t = map(int, input().split())
acnt, ccnt, gcnt, tcnt = 0, 0, 0, 0
ans = 0

for i in range(L):
    if DNA[i] == 'A':
        acnt += 1
    elif DNA[i] == 'C':
        ccnt += 1
    elif DNA[i] == 'G':
        gcnt += 1
    elif DNA[i] == 'T':
        tcnt += 1

if acnt >= a and ccnt >= c and gcnt >= g and tcnt >= t:
    ans +=1

for i in range(1, N-L+1):

    # 앞에 빼고
    if DNA[i-1] == 'A':
        acnt -= 1
    elif DNA[i-1] == 'C':
        ccnt -= 1
    elif DNA[i-1] == 'G':
        gcnt -= 1
    elif DNA[i-1] == 'T':
        tcnt -= 1

    # 뒤에 추가
    if DNA[L-1+i] == 'A':
        acnt += 1
    elif DNA[L-1+i] == 'C':
        ccnt += 1
    elif DNA[L-1+i] == 'G':
        gcnt += 1
    elif DNA[L-1+i] == 'T':
        tcnt += 1

    if acnt >= a and ccnt >= c and gcnt >= g and tcnt >= t:
        ans += 1

print(ans)