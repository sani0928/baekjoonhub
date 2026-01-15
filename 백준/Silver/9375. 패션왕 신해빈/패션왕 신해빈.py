import sys
input = sys.stdin.readline

def solve():
    N = int(input())

    clothes = {}
    ans = 1
    for _ in range(N):
        _, category = map(str, input().split())
        if category in clothes:
            clothes[category] += 1
        else:
            clothes[category] = 1

    for n in clothes.values():
        ans *= (n + 1)
    print(ans - 1)

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        solve()
