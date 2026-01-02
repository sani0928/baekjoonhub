import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = list(input().rstrip())
ans = 0
p_len = N+N+1
mid = p_len//2
p = []
for i in range(p_len):
    if i % 2 == 0:
        p.append('I')
    else:
        p.append('O')

for j in range(mid, len(S) - mid):
    if p == S[j-N:j+N+1]:
        ans += 1
print(ans)
