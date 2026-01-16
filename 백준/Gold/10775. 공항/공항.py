import sys
input = sys.stdin.readline

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
        return
    parent[a] = b
    return

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def docking(max_g):
    global ans, docked

    max_g = find(max_g)
    for g in range(max_g, 0, -1):
        if g in docked:
            continue
        docked.add(g)
        # 한칸 앞으로
        union(g, g - 1)
        ans += 1
        return 1
    return 0

g = int(input())
ans = 0
docked = set()
parent = list(range(g + 1))
for _ in range(int(input())):
    suc = docking(int(input()))
    if not suc:
        break
print(ans)