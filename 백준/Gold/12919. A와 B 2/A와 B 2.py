def recur(word):
    global is_possible

    if is_possible:
        return
    if len(word) == l:
        if word == S:
            is_possible = True
        return
    # 마지막이 A면 마지막 제거
    if word[-1] == 'A':
        recur(word[:-1])
    # 첫번째가 B면 첫번째 제거하고 뒤집기
    if word[0] == 'B':
        recur(word[1:][::-1])

S = list(input().rstrip())
T = list(input().rstrip())
l = len(S)
is_possible = False
recur(T)
if is_possible:
    print(1)
else:
    print(0)