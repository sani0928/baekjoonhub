def cloud_move(d, s):
    lst = set()
    while clouds:
        cx, cy = clouds.pop()
        nx, ny = (cx + dv[0][d] * s) % N , (cy + dv[1][d] * s) % N
        board[nx][ny] += 1
        lst.add((nx, ny))
    return lst

def magic(nx_pos):
    for x, y in nx_pos:
        for d in range(1, 8, 2):
            nx, ny = x + dv[0][d], y + dv[1][d]
            if 0 > nx or 0 > ny or N <= nx or N <= ny or not board[nx][ny]:
                continue
            board[x][y] += 1

def generate_cloud():
    for x in range(N):
        for y in range(N):
            if board[x][y] < 2 or (x, y) in NX:
                continue
            clouds.append((x, y))
            board[x][y] -= 2
            
dv = [(0, -1, -1, -1, 0, 1, 1, 1), (-1, -1, 0, 1, 1, 1, 0, -1)]
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
order = list(tuple(map(int, input().split())) for _ in range(M))
clouds = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]

for D, S in order:
    NX = cloud_move(D-1, S)
    magic(NX)
    generate_cloud()

print(sum(map(sum, board)))