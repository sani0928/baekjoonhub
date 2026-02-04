T = int(input())
while T > 0:
    ans = 0
    N = int(input())
    note = list(map(int, input().split()))
    max_p = note[-1]
    for i in range(N-2, -1, -1):
        if note[i] > max_p:
            max_p = note[i]
            continue
        ans += max_p - note[i]
    print(ans)
    T -= 1