def solve():
    def search(matrix):
        used = [0] * n
        for i in range(1, n):
            diff = matrix[i - 1] - matrix[i]
            if diff == 0:
                continue
            if abs(diff) > 1:
                return 0
            if diff == 1: # matrix[i-1] > matrix[i]
                if i + l > n:
                    return 0
                cur = matrix[i]
                for j in range(i, i + l):
                    if cur != matrix[j] or used[j]:
                        return 0
                for j in range(i, i + l):
                    used[j] = 1
            else: # matrix[i-1] < matrix[i]
                if i - l < 0:
                    return 0
                cur = matrix[i - 1]
                for j in range(i - l, i):
                    if cur != matrix[j] or used[j]:
                        return 0
                for j in range(i - l, i):
                    used[j] = 1
        return 1

    n, l = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    board_reverse = [[board[x][y] for x in range(n)] for y in range(n)]
    ans = 0
    for r in range(n):
        ans += search(board[r])
        ans += search(board_reverse[r])
    print(ans)

if __name__ == '__main__':
    solve()