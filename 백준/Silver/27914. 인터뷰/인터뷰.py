n, k, q = map(int, input().split())
line = [0] + list(map(int, input().split()))
question = list(map(int, input().split()))
ans = [0] * (n + 1)

cnt = 1
for i in range(1, n + 1):
    if line[i] != k:
        ans[i] = ans[i - 1] + cnt
        cnt += 1
    else:
        ans[i] = ans[i - 1]
        cnt = 1
print(*[ans[question[i]] for i in range(q)], sep='\n')