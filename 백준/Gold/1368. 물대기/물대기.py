import sys
input = sys.stdin.readline

def solve():
    def search(ans, cnt):
        for w, u, v in edges:
            if not union(u ,v):
                continue
            ans += w
            cnt += 1
            if cnt == n:
                return ans

    def union(a, b):
        a = find(a)
        b = find(b)
        if a == b:
            return 0
        if size[a] < size[b]:
            a, b = b, a
        size[a] += size[b]
        parent[b] = a
        return 1

    def find(a):
        # 경로 압축
        while a != parent[a]:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    n = int(input())
    self = [0] + list(int(input()) for _ in range(n))

    edges = []
    # 직접 우물을 파는 경우도 고려
    for i in range(1, n + 1):
        edges.append((self[i], 0, i))
    for i in range(1, n + 1):
        lst = [0] + list(map(int, input().split()))
        for j in range(i + 1, n + 1):
            edges.append((lst[j], i, j))
    edges.sort()

    parent, size = list(range(n + 1)), [1] * (n + 1)
    return search(0, 0)

if __name__ == '__main__':
    print(solve())