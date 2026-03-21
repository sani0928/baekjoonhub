def recur(idx, cnt, total):
    if cnt == n:
        res.add(total)
        return
    for i in range(idx, 4):
        recur(i, cnt + 1, total + num[i])

n = int(input())
num = [1, 5, 10, 50]
res = set()
recur(0, 0, 0)
print(len(res))