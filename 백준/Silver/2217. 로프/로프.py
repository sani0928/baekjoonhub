ans = 0; rope = []
N = int(input())
for _ in range(N):
    rope.append(int(input()))
rope.sort()
for i in range(N):
    ans = max(ans, rope[i] * (N - i))
print(ans)