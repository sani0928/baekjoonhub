def recur(idx, cnt):
    global ans

    if cnt > 0 and team[0] == 0:
        return

    if cnt == n // 2:
        team1, team2 = 0, 0
        for i in range(n):
            for j in range(i + 1, n):
                if team[i] != team[j]:
                    continue
                if team[i] and team[j]:
                    team1 += board[i][j]
                    team1 += board[j][i]
                else:
                    team2 += board[i][j]
                    team2 += board[j][i]
        ans = min(ans, abs(team1 - team2))
        return

    for i in range(idx, n):
        team[i] = 1
        recur(i + 1, cnt + 1)
        team[i] = 0

ans = 10 ** 9
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
team = [0] * n
recur(0, 0)
print(ans)