def solve():

    edges = []
    for _ in range(M):
        a, b, t = map(int, input().split())
        edges.append((a, b, t))
        edges.append((b, a, t))
    for _ in range(W):
        a, b, t = map(int, input().split())
        edges.append((a, b, -t))
    dist = [0] * (N + 1)
    for turn in range(1, N + 1):
        change = False
        for u, v, t in edges:
            if dist[v] > dist[u] + t:
                # u를 거쳐 v로 가는 누적 시간이 더 작아지면(dist 감소) 갱신
                dist[v] = dist[u] + t
                change = True
                # 마지막 턴에도 dist가 갱신되었다면 음수 사이클 존재
                if turn == N:
                    return "YES"
        # 갱신이 없으면 NO
        if not change:
            return 'NO'
    return 'NO'

if __name__ == '__main__':
    for _ in range(int(input())):
        N, M, W = map(int, input().split())
        print(solve())