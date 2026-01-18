def solve(char):
    l = len(char)
    moeum = ('a', 'e', 'i', 'o', 'u')
    if not any(c in moeum for c in char):
        # 1번 규칙 위반
        return 0
    if l >= 2:
        for i in range(0, l - 1):
            if char[i] == char[i + 1] and char[i] != moeum[1] and char[i] != moeum[3]:
                # 3번 규칙 위반
                return 0
    if l >= 3:
        for i in range(0, l - 2):
            if char[i] in moeum and char[i + 1] in moeum and char[i + 2] in moeum:
                # 2번 규칙 위반
                return 0
            elif not char[i] in moeum and not char[i + 1] in moeum and not char[i + 2] in moeum:
                # 2번 규칙 위반
                return 0
    return 1

if __name__ == '__main__':
    while True:
        pw = input()
        if pw == 'end':
            break
        if solve(list(map(str, pw.rstrip()))):
            print(f'<{pw}> is acceptable.')
            continue
        print(f'<{pw}> is not acceptable.')