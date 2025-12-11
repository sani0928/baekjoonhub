import sys
input = sys.stdin.readline
# 북,서,남,동
dx, dy = (0,-1,0,1), (1,0,-1,0)
dir_map = {'N':0, 'W':1, 'S':2, 'E':3}
A, B = map(int, input().split())
N, M = map(int, input().split())
robot = {}

grid = [[0] * (A+1) for _ in range(B+1)]

for i in range(1, N+1):
    x, y, d = input().split()
    x, y = int(x), int(y)
    if grid[y][x] != 0:
        print(f'Robot {i} crashes into robot {grid[y][x]}')
        sys.exit(0)
    grid[y][x] = i
    robot[i] = x, y, dir_map[d]

for _ in range(M):
    num, cmd, repeat = input().split()
    num, repeat = int(num), int(repeat)

    cx, cy, cd = robot[num]
    if cmd == 'L':
        cd = (cd + repeat) % 4
        robot[num] = cx, cy, cd
    elif cmd == 'R':
        cd = (cd - repeat) % 4
        robot[num] = cx, cy, cd
    # cmd = F
    else:
        px, py = cx, cy
        for _ in range(repeat):
            nx, ny = cx + dx[cd], cy + dy[cd]
            if not (1 <= nx <= A and 1 <= ny <= B):
                print(f'Robot {num} crashes into the wall')
                sys.exit(0)
            if grid[ny][nx] != 0:
                print(f'Robot {num} crashes into robot {grid[ny][nx]}')
                sys.exit(0)
            cx, cy = nx, ny

        grid[py][px] = 0
        grid[cy][cx] = num
        robot[num] = cx, cy, cd
        
print('OK')