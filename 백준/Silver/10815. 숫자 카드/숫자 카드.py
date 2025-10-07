N = int(input())
hand = set(map(int, input().split()))
M = int(input())
lst = list(map(int, input().split()))

ans = ['1' if num in hand else '0' for num in lst]

print(' '.join(ans))