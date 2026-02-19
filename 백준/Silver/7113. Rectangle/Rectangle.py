import sys; sys.setrecursionlimit(10 ** 6)
def cutting(x, y):
    total = 1
    if x != y:
        if x > y:
            total += cutting(x - y, y)
        else:
            total += cutting(x, y - x)
    return total

n, m = map(int, input().split())
print(cutting(n, m))