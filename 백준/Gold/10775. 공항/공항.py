import sys
input = sys.stdin.readline

def solve():
    def check(g):
        if g != parent[g]:
            parent[g] = check(parent[g])
        return parent[g]
    
    ans = 0
    parent = list(range(int(input()) + 1))
    for _ in range(int(input())):
        gate = check(int(input()))
        if gate == 0:
            return ans
        parent[gate] = check(gate - 1)
        ans += 1
    return ans

if __name__ == '__main__':
    print(solve())