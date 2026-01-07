import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def search(cur):
    global cycle_cnt

    vis[cur] = 1
    nx = parent[cur]
    # 안 가본 노드면 재귀
    if not vis[nx]:
        search(nx)
    else:
        # 사이클 발견
        if not done[nx]:
            x = nx
            # 사이클 포함되는 노드 계산
            while x != cur:
                cycle_cnt += 1
                x = parent[x]
            # 시작 노드도 포함
            cycle_cnt += 1
    # 탐색 완료
    done[cur] = 1
    return

T = int(input())
while T != 0:
    N = int(input())
    cycle_cnt = 0
    project_team = [0] * (N + 1)
    parent = [0] + list(map(int, input().split()))
    vis = [0] * (N + 1)
    done = [0] * (N + 1)

    for u in range(1, N + 1):
        if not vis[u]:
            search(u)
            # print(f'{u}번 노드 탐색 후 사이클 갯수 현황 {cycle_cnt}')
    print(N - cycle_cnt)
    T -= 1