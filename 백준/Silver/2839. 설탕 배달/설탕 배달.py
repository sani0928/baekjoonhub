N = int(input())

def count(N):

    cnt = 0
    if N == 4:
        return -1

    # 5로 딱 나누어 질때까지 3kg 봉투에 담음
    while N % 5 != 0:
        cnt += 1
        N -= 3
        # N이 4가 되면
        if N == 4:
            return -1

    cnt += N // 5

    return cnt

print(count(N))