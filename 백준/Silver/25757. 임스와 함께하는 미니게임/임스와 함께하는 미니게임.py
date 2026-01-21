import sys
input = sys.stdin.readline
def full():
    if g == 'Y':
        return 1
    elif g == 'F':
        return 2
    else:
        return 3
n, g = map(str, input().split())
n, required, players = int(n), full(), set()
for _ in range(n):
    players.add(input().rstrip())
print(len(players) // required)