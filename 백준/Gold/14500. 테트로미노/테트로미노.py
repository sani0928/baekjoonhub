import sys
input = sys.stdin.readline

def solve():

    def back(cr, cc, cnt, total):
        nonlocal ans
        
        vis[cr][cc] = 1
        cnt += 1
        total += board[cr][cc]
        
        if (4 - cnt) * mx_val + total <= ans:
            vis[cr][cc] = 0
            return

        if cnt == 4:
            ans = max(ans, total)
            vis[cr][cc] = 0
            return

        for dr, dc in (0, 1), (1, 0), (0, -1), (-1, 0):
            nr, nc = cr + dr, cc + dc
            if 0 > nr or nr >= n or 0 > nc or nc >= m:
                continue
            if not vis[nr][nc]:
                back(nr, nc, cnt, total)
        vis[cr][cc] = 0
        return

    def check(cr, cc):
        nonlocal ans

        nei_cnt, coord, total = 0, [], board[cr][cc]
        for dr, dc in (0, 1), (1, 0), (0, -1), (-1, 0):
            nr, nc = cr + dr, cc + dc
            if 0 > nr or nr >= n or 0 > nc or nc >= m:
                continue
            nei_cnt += 1
            coord.append((nr, nc))
            total += board[nr][nc]

        if nei_cnt == 4:
            mn = 10 ** 9
            for r, c in coord:
                mn = min(mn, board[r][c])
            ans = max(ans, total - mn)
            return
        elif nei_cnt == 3:
            ans = max(ans, total)
            return
        return

    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    vis = [[0] * m for _ in range(n)]
    mx_val = max(map(max, board))
    ans = -10 ** 9
    for i in range(n):
        for j in range(m):
            back(i, j, 0, 0)
            check(i, j)
    return ans

if __name__ == '__main__':
    print(solve())