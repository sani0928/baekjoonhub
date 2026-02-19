n = int(input())
s = input()
l = 1
for i in range(1, n):
    if abs(ord(s[i - 1]) - ord(s[i])) == 1:
        l += 1
    else:
        l = 1
    if l == 5:
        break
print('YES' if l == 5 else 'NO')