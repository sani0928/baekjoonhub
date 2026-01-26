def solve():
    s = int(input())
    num, ans, r = 0, 0, 1
    while num + r <= s:
        num += r
        r += 1
        ans += 1
    return ans

if __name__ == '__main__':
    print(solve())