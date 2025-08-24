from collections import deque
# while문으로 시간 계산

N, W, L = map(int, input().split())
q = deque(map(int, input().split()))

on_bridge = deque()

t = 0
# 대기 트럭과 다리 위 트럭 둘 중 하나라도 있으면 루프 지속
while q or on_bridge:

    t += 1

    total_w = 0
    # 현재 다리 위에 있는 트럭 이동
    for _ in range(len(on_bridge)):
        time, w = on_bridge.popleft()
        time += 1
        # 아직 다 이동 못 했다면 다리 위에 있으므로 총 중량 체크
        if time < W:
            total_w += w
            on_bridge.append((time, w))


    # 다리 위에 있는 트럭과 올라갈 트럭의 무게가 다리 최대 하중보다 낮다면 대기 트럭 다리 위로 이동
    if q and total_w + q[0] <= L:
        w = q.popleft()
        on_bridge.append((0, w))

print(t)
