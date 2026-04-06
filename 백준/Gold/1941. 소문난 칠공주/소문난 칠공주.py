from collections import deque

def combi(start, s_cnt, total):
    global ans
    if total - s_cnt == 4:
        return
    if total == 7:
        if s_cnt >= 4 and check():
            ans += 1
        return
    for v in range(start, 25):
        selected.append(v)
        x, y = v // n, v % n
        combi(v + 1, s_cnt + 1 if board[x][y] == 'S' else s_cnt, total + 1)
        selected.pop()

def check():
    selected_set = set(selected)
    q = deque([selected[0]])
    vis = {selected[0]}
    while q:
        cv = q.popleft()
        cx, cy = cv // n, cv % n
        for k in range(4):
            nx, ny = cx + dx[k], cy + dy[k]
            if 0 > nx or 0 > ny or n <= nx or n <= ny:
                continue
            nv = nx * n + ny
            if nv in selected_set and nv not in vis:
                vis.add(nv)
                q.append(nv)
    return len(vis) == 7

n = 5
dx, dy = (0, 1, 0, -1), (1, 0, -1 ,0)
board = [input().rstrip() for _ in range(n)]
ans = 0
selected = []

combi(0, 0, 0)
print(ans)