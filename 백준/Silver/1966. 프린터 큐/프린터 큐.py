from collections import deque

T = int(input())

for tc in range(1, T + 1):

    N, M = map(int, input().split())
    # 각 문서에 인덱스 부여
    q = deque(enumerate(map(int, input().split())))
    ans = 0
    cnt = 0

    while True:

        idx, prior = q[0]
        # q에 있는 문서들 중 우선순위가 가장 높다면
        if prior == max(pr for i, pr in q):
            # 출력 카운트 후 프린트
            cnt += 1
            q.popleft()
            # 근데 그게 추적 중인 문서라면
            if idx == M:
                ans = cnt
                break
        # 더 높은 우선순위가 있다면 맨 뒤로
        else:
            q.append(q.popleft())

    print(ans)