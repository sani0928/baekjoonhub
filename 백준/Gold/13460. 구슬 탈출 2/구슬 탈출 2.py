import sys
import copy
input = sys.stdin.readline

ans = 10**9
N, M = map(int, input().split())
MATRIX = [list(map(str, input().rstrip())) for _ in range(N)]

def back(matrix, deep):
    global ans

    # 10번 초과하면 실패
    if deep > 10:
        return

    for d in range(4):
        new_matrix, restball, redgoalin = move(copy.deepcopy(matrix), 2, d)

        if new_matrix == matrix:
            continue

        if restball < 2:
            if restball == 1 and redgoalin:
                ans = min(ans, deep)
            continue

        back(new_matrix, deep + 1)

# 각각의 동작에서 공은 동시에 움직인다. 빨간 구슬이 구멍에 빠지면 성공이지만,
# 파란 구슬이 구멍에 빠지면 실패이다.
# 빨간 구슬과 파란 구슬이 동시에 구멍에 빠져도 실패이다.
# 상하좌우
def move(board, rest, dir):

    red_holein = False
    finding = 0
    
    if dir == 0:
        for j in range(1, M - 1):
            nr = 1
            nc = j
            for i in range(1, N - 1):
                # 공 2개 다 찾으면 종료
                if finding == 2:
                    break
                # 구멍 발견 시 좌표 고정 (중력 반영)
                if board[i][j] == 'O':
                    nr = i
                # 벽 발견 시 그 앞으로 좌표 고정 (중력 반영)
                if board[i][j] == '#':
                    nr = i + 1
                    
                if board[i][j] == 'R':
                    board[i][j] = '.'
                    if board[nr][nc] == 'O':
                       red_holein = True
                       rest -= 1
                    else:
                        board[nr][nc] = 'R'
                        nr += 1

                    finding += 1
                    
                if board[i][j] == 'B':
                    board[i][j] = '.'
                    if board[nr][nc] == 'O':
                        rest -= 1
                    else:
                        board[nr][nc] = 'B'
                        nr += 1

                    finding += 1

    elif dir == 1:
        for j in range(1, M - 1):
            nr = N - 1
            nc = j
            for i in range(N - 1, 0, -1):

                if finding == 2:
                    break

                if board[i][j] == 'O':
                    nr = i

                if board[i][j] == '#':
                    nr = i - 1

                if board[i][j] == 'R':
                    board[i][j] = '.'
                    if board[nr][nc] == 'O':
                       red_holein = True
                       rest -= 1
                    else:
                        board[nr][nc] = 'R'
                        nr -= 1
                    finding += 1

                if board[i][j] == 'B':
                    board[i][j] = '.'
                    if board[nr][nc] == 'O':
                        rest -= 1
                    else:
                        board[nr][nc] = 'B'
                        nr -= 1
                    finding += 1
                    
    elif dir == 2:
        for i in range(1, N - 1):
            nc = 1
            nr = i
            for j in range(1, M - 1):

                if finding == 2:
                    break

                if board[i][j] == 'O':
                    nc = j
                
                if board[i][j] == '#':
                    nc = j + 1

                if board[i][j] == 'R':
                    board[i][j] = '.'
                    if board[nr][nc] == 'O':
                       red_holein = True
                       rest -= 1
                    else:
                        board[nr][nc] = 'R'
                        nc += 1
                    finding += 1

                if board[i][j] == 'B':
                    board[i][j] = '.'
                    if board[nr][nc] == 'O':
                        rest -= 1
                    else:
                        board[nr][nc] = 'B'
                        nc += 1
                    finding += 1
                    
    else:
        for i in range(1, N - 1):
            nc = M - 2
            nr = i
            for j in range(M - 2, 0, -1):

                if finding == 2:
                    break

                if board[i][j] == 'O':
                    nc = j
                
                if board[i][j] == '#':
                    nc = j - 1

                if board[i][j] == 'R':
                    board[i][j] = '.'
                    if board[nr][nc] == 'O':
                       red_holein = True
                       rest -= 1
                    else:
                        board[nr][nc] = 'R'
                        nc -= 1
                    finding += 1

                if board[i][j] == 'B':
                    board[i][j] = '.'
                    if board[nr][nc] == 'O':
                        rest -= 1
                    else:
                        board[nr][nc] = 'B'
                        nc -= 1
                    finding += 1

    return board, rest, red_holein

back(MATRIX, 1)
print(ans if ans != 10**9 else -1)