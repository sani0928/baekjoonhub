import sys
from heapq import *
input = sys.stdin.readline

INF = float('inf')
n = int(input())
board = [list(map(int, input().rstrip())) for _ in range(n)]
hq = []
heappush(hq, (0, 0, 0))
dist = [[INF] * n for _ in range(n)]
dist[0][0] = 0
while hq:
    changed, foot, xy = heappop(hq)
    cr, cc = xy // n, xy % n
    if cr == n - 1 and cc == n - 1:
        print(changed)
        break
    for dr, dc in (0, 1), (1, 0), (0, -1), (-1, 0):
        nr, nc = cr + dr, cc + dc
        if 0 > nr or n <= nr or 0 > nc or n <= nc or dist[nr][nc] <= foot + 1: continue
        dist[nr][nc] = foot + 1
        if board[nr][nc] == 0:
            heappush(hq, (changed + 1, foot + 1, (nr * n) + nc))
            continue
        heappush(hq, (changed, foot + 1, (nr * n) + nc))