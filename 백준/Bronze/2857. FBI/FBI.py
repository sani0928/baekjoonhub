ans = []
for i in range(5):
    name = input().rstrip()
    if 'FBI' in name:
        ans.append(i+1)
print(*ans) if ans else print('HE GOT AWAY!')