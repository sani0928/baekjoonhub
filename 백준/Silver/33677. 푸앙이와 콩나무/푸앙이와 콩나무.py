from collections import deque

def solve():
    def check(nl, nd, nw):
        # 최소 일수 우선 -> 최소 일수가 여러 경우라면 최소 물 양 우선
        if nd < day[nl] or (nd == day[nl] and nw < water[nl]):
            day[nl] = nd
            water[nl] = nw
            q.append(nl)

    n = int(input())
    q = deque([0])
    day = [float('inf')] * (n + 1)
    water = [float('inf')] * (n + 1)
    day[0] = 0
    water[0] = 0
    while q:
        l = q.popleft()
        d = day[l]
        w = water[l]
        if l + 1 <= n:
            check(l + 1, d + 1, w + 1)
        if l * 3 <= n:
            check(l * 3, d + 1, w + 3)
        if l ** 2 <= n:
            check(l ** 2, d + 1, w + 5)

    print(day[n], water[n])
if __name__ == '__main__':
    solve()