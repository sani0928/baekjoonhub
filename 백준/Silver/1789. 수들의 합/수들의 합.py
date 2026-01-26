def solve():
    s = int(input())
    if s == 1 or s == 2:
        return 1
    r, ans = 0, 2
    while True:
        r += ans
        if s <= r + (ans + 1):
            return ans
        ans += 1

if __name__ == '__main__':
    print(solve())