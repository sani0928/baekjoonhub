n, m = map(int, input().split())
cards = []
gift = 0
for _ in range(m):
    a, b = map(int, input().split())
    if a >= n:
        gift += 1
        continue
    cards.append((a, b))
cards.sort(reverse=True)
mn = 0
for w, f in cards:
    if gift >= m - 1:
        break
    mn += n - w
    gift += 1
print(mn)