N, r, c = map(int, input().split())
cnt = 0
l = 2 ** N
# N번 반복하며 분할정복
while N > 0:
    half = l // 2
    block_cnt = half * half

    # z모양 순서대로 0, 1, 2, 3
    if r < half:
        if c < half:
            pos = 0
        else:
            pos = 1
            c -= half
    else:
        if c < half:
            pos = 2
            r -= half
        else:
            pos = 3
            r -= half
            c -= half

    cnt += pos * block_cnt
    l = half
    N -= 1

print(cnt)