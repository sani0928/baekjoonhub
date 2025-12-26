def solution():

    button_a, button_b, button_c = 0, 0, 0
    t = int(input())

    if t % A >= 0:
        button_a += t // A
        t %= A

    if t % B >= 0:
        button_b += t // B
        t %= B

    if t % C >= 0:
        button_c += t // C
        t %= C

    if t > 0:
        return [-1]

    return [button_a, button_b, button_c]

A, B, C = 300, 60, 10
print(*solution())