import sys
input = sys.stdin.readline

def solve():

    def torf(pt, l):
        nonlocal ans
        idx = 0
        while idx < l:
            if t[pt[idx]]:
                ans -= 1
                return
            idx += 1
        return

    ans = M
    t = [0] * (N + 1)
    _, *know = list((map(int, input().split())))
    for i in know:
        t[i] = 1
    parties = []
    for _ in range(M):
        _, *people = list(map(int, input().split()))
        parties.append(people)
    while True:
        change = False
        for party in parties:
            for p in party:
                if t[p]:
                    for p2 in party:
                        if t[p2]:
                            continue
                        change = True
                        t[p2] = 1
        if not change:
            break

    for i in range(M):
        torf(parties[i], len(parties[i]))
    return ans

if __name__ == '__main__':
    N, M = map(int, input().split())
    print(solve())