import sys
input = sys.stdin.readline

def solve():
    def union(a, b):
        a = find(a)
        b = find(b)
        if a < b:
            parent[b] = a
            return
        parent[a] = b
        return

    def find(x):
        if x != parent[x]:
            parent[x] = find(parent[x])
        return parent[x]

    def docking(gate):
        nonlocal ans
        gate = find(gate)
        if gate == 0:
            return 0
        union(gate, gate - 1)
        ans += 1
        return 1

    ans = 0
    parent = list(range(int(input()) + 1))
    for _ in range(int(input())):
        suc = docking(int(input()))
        if not suc:
            return ans
    return ans

if __name__ == '__main__':
    print(solve())