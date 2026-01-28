import sys
input = sys.stdin.readline

def solve():
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    dist = (abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2) ** 0.5
    sum_r = r1 + r2

    if dist == 0:
        if r1 == r2:
            return -1
        return 0
    if r1 == r2:
        if dist > sum_r:
            return 0
        elif dist == sum_r:
            return 1
        return 2
    else:
        mn_r = min(r1, r2)
        mx_r = max(r1, r2)
        if mx_r > dist:
            if dist + mn_r < mx_r:
                return 0
            elif dist + mn_r == mx_r:
                return 1
            return 2
        else:
            if dist > sum_r:
                return 0
            elif dist == sum_r:
                return 1
            return 2

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        print(solve())