import sys
lst = list(map(int, sys.stdin.read().split()))
print('\n'.join('Y' if n % 6 == 0 else 'N' for n in lst))