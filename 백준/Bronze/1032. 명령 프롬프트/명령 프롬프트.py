n = int(input())
init_file = list(input().rstrip())
l = len(init_file)
for _ in range(n - 1):
    file = input().rstrip()
    for i in range(l):
        if init_file[i] == '?':
            continue
        if init_file[i] != file[i]:
            init_file[i] = '?'
print(''.join(init_file))