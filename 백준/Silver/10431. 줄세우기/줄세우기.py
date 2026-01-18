t = int(input())
for tc in range(1, t + 1):
    _, *line = list(map(int, input().split()))
    ans = 0
    for i in range(len(line)):
        for j in range(0, i):
            if line[i] < line[j]:
                ans += i - j
                for k in range(i, j, -1):
                    line[k], line[k -1] = line[k - 1], line[k]
                break
    print(tc, ans)