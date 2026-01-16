import sys
input = sys.stdin.readline

def solve():
    def next_dir(r, c, cmd):
        if cmd == 'U':
            return r + dr[0], c + dc[0]
        elif cmd == 'D':
            return r + dr[1], c + dc[1]
        elif cmd == 'L':
            return r + dr[2], c + dc[2]
        return r + dr[3], c + dc[3]

    def search(cr, cc, num):
        nonlocal ans

        nr, nc = next_dir(cr, cc, g[cr][cc])
        if check[nr][nc]:
            if check[nr][nc] == num:
                ans += 1
            return
        if not check[nr][nc]:
            check[nr][nc] = num
            search(nr, nc, num)
        return

    dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)
    n, m = map(int, input().split())
    g = [list(map(str, input().rstrip())) for _ in range(n)]
    ans, turn = 0, 1
    check = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if check[i][j] != 0:
                continue
            check[i][j] = turn
            search(i, j, turn)
            turn += 1
    return ans

if __name__ == '__main__':
    print(solve())