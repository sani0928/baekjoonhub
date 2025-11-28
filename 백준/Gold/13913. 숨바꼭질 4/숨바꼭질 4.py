from collections import deque

def go():
    global vis
    time = 0
    q = deque([(me, time)])
    vis[me] = time

    while q:
        for _ in range(len(q)):
            cur, time = q.popleft()
            for nx in (cur - 1, cur + 1, cur * 2):
                if 0 <= nx < 100001 and time < vis[nx]:
                    vis[nx] = time + 1
                    q.append((nx, time + 1))
    return

def go2():
    global vis

    if you < me:
        time = me - you
        footprints = list(range(me, you - 1, -1))
        return time, footprints

    q = deque([(me, 0, [me])])

    while q:
        for _ in range(len(q)):
            cur, time, footprints = q.popleft()

            if cur == you:
                return time, footprints

            for nx in (cur - 1, cur + 1, cur * 2):
                if 0 <= nx < 100001 and time + 1 == vis[nx]:
                    q.append((nx, time + 1, footprints + [nx]))
    return False, False

me, you = map(int, input().split())
vis = [10 ** 9] * 100001
go()
ans, ans2 = go2()
print(ans)
print(*ans2)