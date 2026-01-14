N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
white, blue = 0, 0

def search(sr, sc, len):
    global white, blue

    color = matrix[sr][sc]
    for r in range(sr, sr + len):
        for c in range(sc, sc + len):
            if matrix[r][c] != color:
                nx_len = len // 2
                # 4분할
                search(sr, sc, nx_len)
                search(sr, sc + nx_len, nx_len)
                search(sr + nx_len, sc, nx_len)
                search(sr + nx_len, sc + nx_len, nx_len)
                return
    if color == 0:
        white += 1
    else:
        blue += 1
    return

search(0, 0, N)
print(white)
print(blue)