import sys
input = sys.stdin.readline

deck = list(range(27))
n = int(input())
for _ in range(n):
    seq = tuple(map(int, input().split()))
    new_deck = []
    l, r = deck[:13], deck[13:]
    for ch, cnt in enumerate(seq):
        if ch % 2 == 0:
            for _ in range(cnt):
                new_deck.append(r.pop(0))
        else:
            for _ in range(cnt):
                new_deck.append(l.pop(0))
    deck = new_deck
print(deck.index(0) + 1)