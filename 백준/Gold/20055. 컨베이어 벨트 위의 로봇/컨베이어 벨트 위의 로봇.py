n, k = map(int, input().split())
belt = [[i, 0] for i in list(map(int, input().split()))]
LEN = n * 2
cnt = 0
turn = 0
while cnt < k:
    # 1-1) 벨트 이동
    belt.insert(0, belt.pop())
    # 1-2) 내리는 위치에 로봇 있으면 내림
    if belt[n-1][1]:
        belt[n-1][1] = 0
    # 2) 순서대로 벨트 위 로봇 이동
    for i in range(n - 2, -1, -1):
        if not belt[i][1]:
            continue
        nx = i + 1
        if not belt[nx][1] and belt[nx][0] >= 1:
                belt[i][1] = 0
                belt[nx][1] = 1 if nx != n-1 else 0
                belt[nx][0] -= 1
                if belt[nx][0] == 0:
                    cnt += 1
    # 3) 올리는 위치에 로봇 올리기
    if belt[0][0] >= 1:
        belt[0][1] = 1
        belt[0][0] -= 1
        if belt[0][0] == 0:
            cnt += 1
    turn += 1

print(turn)