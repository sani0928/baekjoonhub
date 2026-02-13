import sys
input = sys.stdin.readline

def solve(a, b, c):
    if a == b and b == c: return 'Equilateral'
    if a + b <= c: return 'Invalid'
    if a == b or b == c: return 'Isosceles'
    return 'Scalene'

while True:
    lens = list(map(int, input().split()))
    if lens[0]:
        lens.sort()
        print(solve(lens[0], lens[1], lens[2]))
        continue
    break