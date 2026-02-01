board = list(input().rstrip()) + ['.']
i, s = 0, 0
success = True
while i < len(board):
    if s == 4:
        for j in range(i - 4, i):
            board[j] = 'A'
        s = 0
    if board[i] == 'X':
        s += 1
    else:
        if s == 4:
            for j in range(i - 4, i):
                board[j] = 'A'
        elif s == 2:
            for j in range(i - 2, i):
                board[j] = 'B'
        elif s == 1 or s == 3:
            success = False
            break
        s = 0
    i += 1
    
if success:
    print(''.join(board[:-1]))
else:
    print(-1)