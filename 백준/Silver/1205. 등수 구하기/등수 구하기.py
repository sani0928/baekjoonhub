from collections import defaultdict
# 문제 : 등수 구하기
# 티어 : Silver IV

def solve():
    n, new, p = map(int, input().split())
    i = 0
    if i < n:
        rank = list(map(int, input().split()))
        order = defaultdict(int)
        while i < n and rank[i] >= new:
            if not order[rank[i]]:
                order[rank[i]] = i + 1
            i += 1
        if i + 1 <= p:
            if order[new]:
                return order[new]
            return i + 1
        return -1
    return 1

if __name__ == '__main__':
    print(solve())