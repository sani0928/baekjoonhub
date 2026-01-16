import sys, heapq
input = sys.stdin.readline

def solve():
    C, N = map(int, input().split())
    arr = []
    for _ in range(N):
        cost, num = map(int, input().split())
        arr.append((cost, num))

    def search(hq):
        ans = 10 ** 9
        v = [10 ** 9] * C
        heapq.heappush(hq, (0, 0))
        while hq:
            c, n = heapq.heappop(hq)
            for i in range(N):
                nc, nn = c + arr[i][0], n + arr[i][1]
                if nn >= C:
                    ans = min(ans, nc)
                    continue
                if nc < v[nn]:
                    v[nn] = nc
                    heapq.heappush(hq, (nc, nn))
        return ans
    return search([])

if __name__ == '__main__':
    print(solve())