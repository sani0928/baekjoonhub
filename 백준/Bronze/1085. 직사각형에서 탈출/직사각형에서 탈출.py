x, y, w, h = map(int, input().split())

if x > w // 2:
    if y > h // 2:
        print(min(w-x, h-y))
    else:
        print(min(w-x, y))
elif x <= w // 2:
    if y > h // 2:
        print(min(x, h-y))
    else:
        print(min(x, y))