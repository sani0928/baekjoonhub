from collections import defaultdict

n = int(input())
arrange = defaultdict(int)
for _ in range(n):
    name = input().split('.')[1]
    arrange[name] += 1
for file in sorted(arrange):
    print(file, arrange[file])