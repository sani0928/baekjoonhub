N = int(input())
s = []
cur = 0
answer = []
for _ in range(N):
    num = int(input())

    if cur < num:
        for i in range(cur + 1, num + 1):
            answer.append('+')
            cur += 1
            s.append(i)

    if s[-1] == num:
        answer.append('-')
        s.pop()

if s:
    print('NO')
else:
    for ans in answer:
        print(ans)