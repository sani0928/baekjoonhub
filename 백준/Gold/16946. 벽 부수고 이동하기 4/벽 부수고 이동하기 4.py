from collections import deque

def componentize(sr, sc, idx):

    cnt = 1
    q = deque([(sr, sc)])
    while q:
        cr, cc = q.popleft()
        for dr, dc in (0, 1), (1, 0), (0, -1), (-1, 0):
            nr, nc = cr + dr, cc+ dc
            if 0 <= nr < N and 0 <= nc < M and not matrix[nr][nc]:
                if not avail_comp[nr][nc]:
                    avail_comp[nr][nc] = idx
                    cnt += 1
                    q.append((nr, nc))
    return cnt

def counting(br, bc):

    cnt = 1
    seen = set()
    for dr, dc in (0, 1), (1, 0), (0, -1), (-1, 0):
        nr, nc = br + dr, bc + dc
        if 0 <= nr < N and 0 <= nc < M and not matrix[nr][nc]:
            id = avail_comp[nr][nc]
            if not id in seen:
                seen.add(id)
                cnt += avail_comp_label[id]
    return cnt

MOD = 10
N, M = map(int, input().split())
res = [[0] * M for _ in range(N)]
available = []
block = []
matrix = []
avail_comp = [[0] * M for _ in range(N)]
avail_comp_label = [0]
for r in range(N):
    row = list(map(int, input().rstrip()))
    for c, cell in enumerate(row):
        if cell == 1:
            block.append((r, c))
        else:
            available.append((r, c))
    matrix.append(row)

label = 0
for r, c in available:
    if not avail_comp[r][c]:
        label += 1
        avail_comp[r][c] = label
        avail_comp_label.append(componentize(r, c, label))

for r, c in block:
    res[r][c] = counting(r, c) % MOD

for r in res:
    print(''.join(map(str, r)))