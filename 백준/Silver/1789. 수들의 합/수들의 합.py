def solve():
    s = int(input())
    r, ans = 1, 1
    while True:
        r += 1
        if s < (r * (r + 1)) // 2:
            return ans
        ans += 1

if __name__ == '__main__':
    print(solve())