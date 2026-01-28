import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    freq = {}
    for _ in range(n):
        w = input().rstrip()
        if len(w) < m:
            continue
        if w in freq:
            freq[w] += 1
        else:
            freq[w] = 1
    for char in sorted(list(freq.keys()), key=lambda c: (-freq[c], -len(c), c)):
        print(char)

if __name__ == '__main__':
    solve()