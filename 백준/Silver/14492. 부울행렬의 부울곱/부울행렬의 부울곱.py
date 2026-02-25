n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]
B = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            if A[i][k] and B[k][j]:
                ans += 1
                break
print(ans)