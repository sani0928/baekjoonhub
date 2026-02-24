import sys; from collections import defaultdict
input = sys.stdin.readline
n = int(input())
arrange = defaultdict(int)
for _ in range(n):
    name = input().rstrip().split('.')[1]
    arrange[name] += 1
for file in sorted(arrange):
    print(file, arrange[file])