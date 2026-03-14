def recur(idx, cnt):
    global ans

    if cnt == n // 2:
        team1, team2 = [], []
        for i in range(n):
            if team[i]:
                team1.append(i)
            else:
                team2.append(i)
        t1, t2 = 0, 0
        for i in range(n // 2):
            for j in range(i + 1, n // 2):
                t1 += scores[team1[i]][team1[j]]
        for i in range(n // 2):
            for j in range(i + 1, n // 2):
                t2 += scores[team2[i]][team2[j]]
        ans = min(ans, abs(t1 - t2))
        return

    for i in range(idx, n):
        team[i] = 1
        recur(i + 1, cnt + 1)
        team[i] = 0

ans = 10 ** 9
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
scores = [[board[i][j] + board[j][i] for j in range(n)] for i in range(n)]
team = [0] * n
team[0] = 1
recur(1, 1)
print(ans)