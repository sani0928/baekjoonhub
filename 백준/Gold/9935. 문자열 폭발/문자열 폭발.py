text = list(map(str, input().strip()))
bomb_text = list(map(str, input().strip()))
text_len = len(text)
bomb_len = len(bomb_text)

s = []

for i in range(text_len):

    s.append(text[i])
    s_len = len(s)

    if s_len >= bomb_len:
        if s[s_len-bomb_len:s_len] == bomb_text:
            for _ in range(bomb_len):
                s.pop()

if s:
    print(''.join(s))
else:
    print('FRULA')