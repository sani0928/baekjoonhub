n = int(input())
arr = [0] + list(map(int, input().split()))
ans = []
v = [0] * (n + 1)
order = 0
while order != n:
    for i in range(1, n + 1):
        if not v[i] and arr[i] == 0:
            v[i] = 1
            ans.append(i)
            order += 1
            for j in range(1, i):
                if arr[j] != 0:
                    arr[j] -= 1
            break
print(*ans)