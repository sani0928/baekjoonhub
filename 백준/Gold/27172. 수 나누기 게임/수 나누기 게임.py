n = int(input())
arr = list(map(int, input().split()))
mx_val = max(arr)
score = [0] * n
players = [-1] * (mx_val + 1)

for i, v in enumerate(arr):
    players[v] = i

for i, v in enumerate(arr):
    for nx in range(v * 2, mx_val + 1, v):
        j = players[nx]
        if j != -1:
            score[i] += 1
            score[j] -= 1
print(*score)