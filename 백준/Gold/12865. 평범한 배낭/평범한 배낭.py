import sys
input = sys.stdin.readline
N, K = map(int, input().split())
comp = [0] * (K + 1)
for _ in range(N):
    w, v = map(int, input().split())
    for i in range(K, w - 1, -1):
        comp[i] = max(comp[i], comp[i - w] + v)
print(comp[K])