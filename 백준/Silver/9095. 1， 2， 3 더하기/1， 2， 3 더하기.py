def solve():
    N = int(input())
    ans = 0

    def back(n):
        nonlocal ans
        if n == 0:
            ans += 1
            return
        for i in range(1, 4):
            if n - i >= 0:
                back(n - i)
    back(N)
    print(ans)

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        solve()