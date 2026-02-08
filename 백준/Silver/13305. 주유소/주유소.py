N = int(input())
dist = list(map(int, input().split()))
country = list(map(int, input().split()))

min_cost = 10**9
cur_dist = 0
total = 0

for i in range(N-2, -1, -1):
    min_cost = min(min_cost, country[i])
    cur_dist += dist[i]

    if country[i] > min_cost:
        total += country[i] * dist[i]
    else:
        total = country[i] * cur_dist

print(total)