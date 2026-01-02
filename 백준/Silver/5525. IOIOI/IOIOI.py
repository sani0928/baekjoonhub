N = int(input())
M = int(input())
S = tuple(map(str, input().strip()))

ans = 0

sample = []
for i in range(N*2+1):
    if i % 2 == 0:
        sample.append('I')
    else:
        sample.append('O')

for j in range(len(S)):
    if S[j] == 'I':
        idx = 0
        result = True
        while idx < N*2+1:
            if j >= len(S) or S[j] != sample[idx]:
                result = False
                break

            idx += 1
            j += 1

        if result:
            ans += 1

print(ans)