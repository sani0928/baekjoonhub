import heapq

N = int(input())

people = []
for idx in range(N):
    age, name = map(str, input().split())
    heapq.heappush(people, (int(age), idx, name))

for _ in range(N):
    a, i, n = heapq.heappop(people)
    print(a, n)