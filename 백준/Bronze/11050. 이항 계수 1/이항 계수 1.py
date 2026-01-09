import sys
input = sys.stdin.readline
def ft1(n, k):
    res = n
    for x in range(n - 1, k, -1):
        res *= x
    return res
def ft2(n):
    res = n
    for x in range(n - 1, 1, -1):
        res *= x
    return res
N, K = map(int, input().split())
K = min(K, N-K)
print(ft1(N, K) // ft2(N - K))