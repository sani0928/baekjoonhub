ans = 0
N = int(input())
rope = [int(input()) for _ in range(N)]
rope.sort()
for i in range(N):
    ans = max(ans, rope[i] * (N - i))
print(ans)