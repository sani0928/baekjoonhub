from collections import deque

def solve():
    def back(idx, cnt, soldier):
        nonlocal ans
        if cnt == 3:
            res = game(soldier, 0, enemy_cnt)
            ans = max(ans, res)
            return
        for i in range(idx, m):
            back(i + 1, cnt + 1, soldier + [(n, i)])

    def game(p, kill, rest):
        matrix = [l[:] for l in board]
        while rest != 0:
            target = set()
            for x, y in p:
                q = deque([(x - 1, y, 1)])
                v = [[0] * m for _ in range(n)]
                v[x - 1][y] = 1
                while q:
                    cx, cy, foot = q.popleft()
                    if foot > d:
                        continue
                    if matrix[cx][cy] == 1:
                        target.add((cx, cy))
                        break

                    for dx, dy in (0, -1), (-1, 0), (0, 1):
                        nx, ny = cx + dx, cy + dy
                        if nx < 0 or nx >= n or ny < 0 or ny >= m or v[nx][ny]:
                            continue
                        v[nx][ny] = 1
                        q.append((nx, ny, foot + 1))

            new_matrix = [[0] * m for _ in range(n)]
            for x in range(n - 1, -1, -1):
                for y in range(m):
                    if (x, y) in target:
                        rest -= 1
                        kill += 1
                        continue
                    if matrix[x][y] == 1:
                        if x + 1 == n:
                            rest -= 1
                            continue
                        new_matrix[x + 1][y] = 1
            matrix = new_matrix
        return kill

    n, m, d = map(int, input().split())
    board, enemy_cnt = [], 0
    for r in range(n):
        row = list(map(int, input().split()))
        for c in range(m):
            if row[c] == 1:
                enemy_cnt += 1
        board.append(row)
    ans = 0
    back(0, 0, [])
    print(ans)

if __name__ == '__main__':
    solve()