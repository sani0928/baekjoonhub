import sys

N, M = map(int, input().split())
name_to_num = {}
num_to_name = {}
for num in range(1, N + 1):
    name = sys.stdin.readline().strip()
    name_to_num[name] = num
    num_to_name[num] = name
for _ in range(M):
    question = sys.stdin.readline().strip()
    if question.isdigit():
        print(num_to_name[int(question)])
    else:
        print(name_to_num[question])