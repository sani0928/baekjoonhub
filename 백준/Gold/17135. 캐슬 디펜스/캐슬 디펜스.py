from collections import deque

def solve():
    def back(idx, cnt, soldier):
        nonlocal ans
        if cnt == 3:
            res = game(soldier, 0)
            ans = max(ans, res)
            return
        for i in range(idx, m):
            back(i + 1, cnt + 1, soldier + [(n, i)])

    def game(p, kill):
        matrix = [row[:] for row in board]
        while True:
            target = set()
            # 타켓 설정
            for x, y in p:
                q = deque([(x - 1, y, 1)])
                v = [[0] * m for _ in range(n)]
                v[x-1][y] = 1
                while q:
                    cx, cy, foot = q.popleft()

                    if matrix[cx][cy] == 1:
                        target.add((cx, cy))
                        break
                    if foot == d:
                        continue

                    for dx, dy in (0, -1), (-1, 0), (0, 1):
                        nx, ny = cx + dx, cy + dy
                        if nx < 0 or nx >= n or ny < 0 or ny >= m or v[nx][ny]:
                            continue
                        v[nx][ny] = 1
                        q.append((nx, ny, foot + 1))

            rest = 0
            new_matrix = [[0] * m for _ in range(n)]
            for r in range(n - 1, -1, -1):
                for c in range(m):
                    # 타켓이라면 제거
                    if (r, c) in target:
                        kill += 1
                        continue
                    # 남은 적들 이동
                    if matrix[r][c] == 1:
                        if r + 1 != n:
                            rest += 1
                            new_matrix[r + 1][c] = 1
            if not rest:
                break
            matrix = new_matrix
        return kill

    n, m, d = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    back(0, 0, [])
    print(ans)

if __name__ == '__main__':
    solve()