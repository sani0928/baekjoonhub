def d(n):
    nx = n + sum(map(int, str(n)))
    if nx >= 10 ** 4:
        return
    if check[nx]:
        return
    check[nx] = 1

check = [0] * (10 ** 4)
for i in range(1, 10 ** 4):
    d(i)
for i in range(1, 10 ** 4):
    if not check[i]:
        print(i)