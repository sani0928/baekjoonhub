N = int(input())
people = []
ans = [0] * N
for idx in range(N):
    weight, length = map(int, input().split())
    people.append((idx, weight, length))

for i, x, y in people:
    rank = 0
    for j in range(N):
        if i == j:
            continue
        _, p, q = people[j]
        if p > x and q > y:
            rank += 1
    ans[i] = rank + 1
print(*ans)