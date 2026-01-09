N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda x : (x[1], x[0]))
for x, y in arr:
    print(x, y)