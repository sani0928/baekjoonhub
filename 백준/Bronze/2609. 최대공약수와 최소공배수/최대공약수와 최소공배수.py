n1, n2 = map(int, input().split())
ans1 = min(n1, n2)
while True:
    if n1 % ans1 == 0 and n2 % ans1 == 0:
        print(ans1)
        break
    ans1 -= 1
print((n1 * n2) // ans1)