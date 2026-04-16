n = int(input())
cost = [int(input()) for _ in range(n)]
m = int(input())
print(sum([cost[int(input()) - 1] for _ in range(m)]))