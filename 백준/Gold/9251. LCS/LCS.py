s1 = '0' + input().rstrip()
s2 = '0' + input().rstrip()
matrix = [[0] * len(s1) for _ in range(len(s2))]

for c in range(1, len(s1)):
    for r in range(1, len(s2)):
        if s1[c] == s2[r]:
            matrix[r][c] = matrix[r-1][c-1] + 1
        else:
            matrix[r][c] = max(matrix[r-1][c], matrix[r][c-1])

print(matrix[len(s2) - 1][len(s1) - 1])