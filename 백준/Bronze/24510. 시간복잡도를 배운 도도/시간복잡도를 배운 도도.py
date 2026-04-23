n = int(input())
data = [input().rstrip() for _ in range(n)]
ans = 0
for s in data:
    cnt = s.count('for') + s.count('while')
    ans = max(ans, cnt)
print(ans)