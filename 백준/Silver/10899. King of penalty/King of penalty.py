p, n = map(int, input().split())
tt = list(map(int, input().split()))
tt.sort()
submit = 0
score = 0
penalty = p - 1
for i in range(n):
    if penalty <= tt[i]:
        break
    score += penalty
    penalty -= tt[i]
    submit += 1
print(submit, score)