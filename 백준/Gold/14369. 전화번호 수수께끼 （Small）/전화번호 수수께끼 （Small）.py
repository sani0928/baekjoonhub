import sys
from collections import defaultdict, Counter
input = sys.stdin.readline

def solve():
    def search(word, number):
        nonlocal ans, flag

        cnt2 = Counter(word)
        while True:
            for k in cnt2.keys():
                if cnt[k] < cnt2[k]:
                    return
            ans += str(number)
            for k in cnt2.keys():
                cnt[k] -= cnt2[k]
                flag -= cnt2[k]

    note = [
        ('ZERO', 0), ('TWO', 2), ('FOUR', 4), ('SIX', 6), ('EIGHT', 8),
        ('ONE', 1), ('THREE', 3), ('FIVE', 5), ('SEVEN', 7), ('NINE', 9)
    ]

    in_put = input().rstrip()
    cnt = defaultdict(int)
    flag = len(in_put)
    for c in in_put:
        cnt[c] += 1
    ans = []
    for s, n in note:
        if not flag:
            return ''.join(sorted(ans))
        search(s.rstrip(), n)
    return ''.join(sorted(ans))

if __name__ == '__main__':
    T = int(input())
    for tc in range(1, T + 1):
        print(f'Case #{tc}: {solve()}')