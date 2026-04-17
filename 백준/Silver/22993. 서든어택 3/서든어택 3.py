n = int(input())
me, *other = list(map(int, input().split()))
other.sort()
ans = 'Yes'
for i in range(n-1):
    if me <= other[i]:
        ans = 'No'
        break
    me += other[i]
print(ans)