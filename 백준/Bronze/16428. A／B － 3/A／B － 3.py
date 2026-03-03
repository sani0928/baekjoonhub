a, b = map(int, input().split())
print((a - (a % abs(b))) // b)
print(a % abs(b))