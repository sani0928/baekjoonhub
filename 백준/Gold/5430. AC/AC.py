from collections import deque

def solve():
    p = list(map(str, input().rstrip()))
    n = int(input())
    arr = input()
    if n == 0:
        arr = deque()
    else:
        arr = deque(map(int, arr[1:-1].split(',')))

    rev = False

    for cmd in p:
        if cmd == 'R':
            rev = not rev
        else:
            if not arr:
                print('error')
                return
            if rev:
                arr.pop()
                continue
            arr.popleft()

    if rev:
        arr.reverse()

    print('[' + ','.join(map(str, arr)) + ']')

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        solve()