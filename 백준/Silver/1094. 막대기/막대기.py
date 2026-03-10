def solve():
    x = int(input())
    if x == 64:
        return 1
    candi = [32, 16, 8, 4, 2, 1]
    ans = 0
    for i in range(6):
        if x == 0:
            return ans
        if x - candi[i] >= 0:
            x -= candi[i]
            ans += 1
    return ans

if __name__ == '__main__':
    print(solve())