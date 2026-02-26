import sys
from collections import deque
input = sys.stdin.readline
q = deque()
for _ in range(int(input())):
    ip = input().split()
    cmd = ip[0]
    if cmd == 'push':
        q.append(int(ip[1]))
        continue
    if cmd == 'pop':
        if q:
            print(q.popleft())
        else:
            print(-1)
        continue
    if cmd == 'size':
        print(len(q))
    if cmd == 'empty':
        if q:
            print(0)
        else:
            print(1)
        continue
    if cmd =='front':
        if q:
            print(q[0])
        else:
            print(-1)
        continue
    if cmd == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)