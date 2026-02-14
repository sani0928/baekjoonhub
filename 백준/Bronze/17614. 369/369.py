n = int(input())
ans = 0
for i in range(1, n + 1):
    i = str(i)
    ans += i.count('3')
    ans += i.count('6')
    ans += i.count('9')
print(ans)