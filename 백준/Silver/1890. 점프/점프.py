import sys
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
record = [[0] * N for _ in range(N)]
record[0][0] = 1
for r in range(N):
    for c in range(N):
        if record[r][c] == 0:
            continue
        jump = board[r][c]
        if jump == 0:
            continue
        for dr, dc in (0, 1), (1, 0):
            nr, nc = r + dr * jump, c + dc * jump
            if nr >= N or nc >= N:
                continue
            record[nr][nc] += record[r][c]
print(record[N-1][N-1])