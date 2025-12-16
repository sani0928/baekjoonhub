N = int(input())
ans = 0
for _ in range(N):
    string = input().rstrip()
    seen = set()
    cnt = True
    last = string[0]
    seen.add(last)
    for char in string:
        if char != last:
            if char in seen:
                cnt = False
                break
            else:
                seen.add(char)
                last = char
    if cnt:
        ans += 1
print(ans)