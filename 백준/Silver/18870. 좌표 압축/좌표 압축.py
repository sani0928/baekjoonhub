N = int(input())
coords = list(map(int, input().split()))
check = sorted(set(coords))
ordered = {num : order for order, num in enumerate(check)}
print(*[ordered[coords[i]] for i in range(N)])