lst = []
n = int(input())
for _ in range(n):
    name, d, m, y = map(str, input().split())
    lst.append((int(y), int(m), int(d), name))
lst.sort()
print(lst[-1][3])
print(lst[0][3])