def calcul():
    res = 1
    for i in range(n):
        if res != arr[i]:
            return res
        res += 1
        i += 1
    return res

n = int(input())
arr = sorted(map(int, input().split()))
print(calcul())