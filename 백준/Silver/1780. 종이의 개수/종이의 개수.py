import sys

def solve():
    N = int(sys.stdin.readline())
    matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    paper1, paper2, paper3 = 0, 0, 0

    def search(sr, sc, len):
        nonlocal paper1, paper2, paper3

        paper = matrix[sr][sc]
        for r in range(sr, sr + len):
            for c in range(sc, sc + len):
                if matrix[r][c] != paper:
                    nx_len = len // 3
                    for sector1 in range(3):
                        for sector2 in range(3):
                            search(sr + (sector1 * nx_len), sc + (sector2 * nx_len), nx_len)
                    return
        if paper == -1:
            paper1 += 1
        elif paper == 0:
            paper2 += 1
        else:
            paper3 += 1
        return

    search(0, 0, N)
    print(paper1, paper2, paper3, sep='\n')

if __name__ == '__main__':
    solve()