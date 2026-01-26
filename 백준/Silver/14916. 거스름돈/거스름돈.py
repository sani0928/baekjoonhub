import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    if n == 1 or n == 3:
        return -1

    if n % 5 == 0:
        return n // 5

    if n // 5 < 2 and n % 2 == 0:
        return n // 2

    ans = 0
    while n % 5 != 0:
        n -= 5
        ans += 1
        if n // 5 < 2 and n % 2 == 0:
            ans += n // 2
            return ans

if __name__ == '__main__':
    print(solve())