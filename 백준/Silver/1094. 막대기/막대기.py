def solve():
    x = int(input())
    if x == 64:
        return 1
    candi = 32
    total = 0
    ans = 0
    while total != x:
        if total + candi <= x:
            total += candi
            ans += 1
        candi //= 2
    return ans

if __name__ == '__main__':
    print(solve())