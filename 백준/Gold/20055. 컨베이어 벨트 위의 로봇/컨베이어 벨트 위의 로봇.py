n, k = map(int, input().split())
belt = list(map(int, input().split()))
LEN = n * 2
pos = [0] * LEN
cnt = 0
turn = 0
while cnt < k:
    # 1-1) 벨트 이동
    belt.insert(0, belt.pop())
    pos.insert(0, pos.pop())
    # 1-2) 내리는 위치에 로봇 있으면 내림
    if pos[n-1]:
        pos[n-1] = 0
    # 2-1) 순서대로 벨트 위 로봇 이동
    for i in range(n - 2, -1, -1):
        if not pos[i]:
            continue
        nx = i + 1
        if not pos[nx] and belt[nx] >= 1:
                pos[i] = 0
                pos[nx] = 1
                belt[nx] -= 1
                if belt[nx] == 0:
                    cnt += 1
    # 2-2) 내리는 위치에 로봇 있으면 내림
    if pos[n-1]:
        pos[n-1] = 0
    # 3) 올리는 위치에 로봇 올리기
    if belt[0] >= 1:
        pos[0] = 1
        belt[0] -= 1
        if belt[0] == 0:
            cnt += 1
    turn += 1

print(turn)