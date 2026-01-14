N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
white, blue = 0, 0

def first():
    all = N**2
    total_w, total_b = 0, 0
    for r in range(N):
        for c in range(N):
            if matrix[r][c] == 0:
                total_w += 1
            else:
                total_b += 1
    if total_w == all:
        return 1, 0
    elif total_b == all:
        return 0, 1
    return 0, 0



def check(sr, er, sc, ec, l):
    all = l**2
    total_w, total_b = 0, 0
    for r in range(sr, er):
        for c in range(sc, ec):
            if matrix[r][c] == 0:
                total_w += 1
            else:
                total_b += 1
    if total_w == all:
        return 1, 0
    elif total_b == all:
        return 0, 1
    return 0, 0

def back(mid_r, mid_c, l):
    global white, blue

    if l == 0:
        return

    check1, check2, check3, check4 = False, False, False, False
    for i in range(4):
        if i == 0:
            w, b = check(mid_r - l, mid_r, mid_c - l, mid_c, l)
            if w or b:
                check1 = True
                if w:
                    white += 1
                else:
                    blue += 1

        elif i == 1:
            w, b = check(mid_r - l, mid_r, mid_c, mid_c + l, l)
            if w or b:
                check2 = True
                if w:
                    white += 1
                else:
                    blue += 1

        elif i == 2:
            w, b = check(mid_r, mid_r + l, mid_c - l, mid_c, l)
            if w or b:
                check3 = True
                if w:
                    white += 1
                else:
                    blue += 1

        else:
            w, b = check(mid_r, mid_r + l, mid_c, mid_c + l, l)
            if w or b:
                check4 = True
                if w:
                    white += 1
                else:
                    blue += 1

    if not check1:
        back(mid_r - (l // 2), mid_c - (l // 2), l // 2)
    if not check2:
        back(mid_r - (l // 2), mid_c + (l // 2), l // 2)
    if not check3:
        back(mid_r + (l // 2), mid_c - (l // 2), l // 2)
    if not check4:
        back(mid_r + (l // 2), mid_c + (l // 2), l // 2)
    return

W, B = first()
if W or B:
    if W:
        print(1)
        print(0)
    else:
        print(0)
        print(1)
else:
    back(N // 2, N // 2, N // 2)
    print(white)
    print(blue)