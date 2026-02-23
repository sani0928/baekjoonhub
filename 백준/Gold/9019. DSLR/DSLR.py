import sys; from collections import deque
input = sys.stdin.readline

def solve():
    def d(num): return (num * 2) % 10000
    def s(num): return num - 1 if num != 0 else 9999
    def l(num): return (num % 1000) * 10 + (num // 1000)
    def r(num): return (num % 10) * 1000 + (num // 10)
    start, final = map(int, input().split())
    prev = [-1] * 10000
    rec = [''] * 10000
    q = deque([start])
    prev[start] = start
    while q:
        cur = q.popleft()
        if cur == final:
            break
        for nx, cmd in (d(cur), 'D'), (s(cur), 'S'), (l(cur), 'L'), (r(cur), 'R'):
            if prev[nx] != -1:
                continue
            prev[nx] = cur
            rec[nx] = cmd
            q.append(nx)

    cur = final
    ans = []
    while cur != start:
        ans.append(rec[cur])
        cur = prev[cur]
    ans.reverse()
    return ans

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        print(''.join(solve()))