def bingo():

    x, o = False, False
    win_situation = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]

    for pos in win_situation:
        if case[pos[0]] == case[pos[1]] == case[pos[2]] and case[pos[0]] != '.':
            if case[pos[0]] == 'X':
                x = True
            else:
                o = True
    return x, o

def is_hol():
    x_cnt = case.count('X')
    o_cnt = case.count('O')
    if x_cnt == o_cnt + 1:
        return True
    else:
        return False

def is_jjak():
    x_cnt = case.count('X')
    o_cnt = case.count('O')
    if x_cnt == o_cnt:
        return True
    else:
        return False

while True:
    case = input()
    if case == 'end':
        break

    total = 9 - case.count('.')
    x_win, o_win = bingo()

    # 9칸 모두 채워졌는데 백이 이겼다면 유효x
    if total == 9 and o_win:
        print('invalid')
        continue

    # 둘 다 이길 순 없음
    if x_win and o_win:
        print('invalid')
        continue

    # 흑 혹은 백이 빙고라면 유효성 확인 (흑이 이겼으면 홀, 백이 이겼으면 짝)
    if x_win or o_win:
        if x_win:
            if total % 2 != 0 and is_hol():
                print('valid')
            else:
                print('invalid')
        else:
            if total % 2 == 0 and is_jjak():
                print('valid')
            else:
                print('invalid')
    # 둘다 빙고가 아니라면 유효성 확인 (9칸 다 채운거면 유효)
    else:
        if total == 9 and is_hol():
            print('valid')
        else:
            print('invalid')