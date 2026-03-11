def recur(total, lst):
    global ans
    if len(lst) == 2:
        ans = max(ans, total)
        return

    for i in range(1, len(lst) - 1):
        energy = lst[i-1] * lst[i+1]
        popped = lst.pop(i)
        recur(total + energy, lst)
        lst.insert(i, popped)

n = int(input())
arr = list(map(int, input().split()))
ans = 0
recur(0, arr)
print(ans)