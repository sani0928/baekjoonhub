N, M = map(int, input().split())
saving = {}
for _ in range(N):
    name, pw = map(str, input().split())
    saving[name] = pw
for _ in range(M):
    print(saving[input()])