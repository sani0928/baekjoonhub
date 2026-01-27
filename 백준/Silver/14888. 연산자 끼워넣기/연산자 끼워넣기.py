import sys
input = sys.stdin.readline

def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    if a < 0:
        return -(-a // b)
    return a // b

def cal(res, cur):
    global mn, mx

    if cur == n:
        mn = min(mn, res)
        mx = max(mx, res)
        return

    for i in range(4):
        if not rest[i]:
            continue
        rest[i] -= 1
        cal(opers[i](res, num[cur]), cur + 1)
        rest[i] += 1

n = int(input())
num = list(map(int, input().split()))
rest = list(map(int, input().split()))

mx, mn = -10**9, 10 ** 9
opers = [add, sub, mul, div]
cal(num[0], 1)
print(mx, mn, sep='\n')