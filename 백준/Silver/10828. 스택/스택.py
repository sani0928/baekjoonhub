N = int(input())
s = []
ans = []

for _ in range(N):
    command = input().split()
    if command[0] == 'push':
        s.append(command[1])
    elif command[0] == 'pop':
        if len(s) == 0:
            ans.append('-1')
            continue
        ans.append(s.pop())
    elif command[0] == 'size':
        ans.append(str(len(s)))
    elif command[0] == 'empty':
            ans.append('0' if s else '1')
    elif command[0] == 'top':
        ans.append(s[-1] if s else '-1')

print('\n'.join(ans))