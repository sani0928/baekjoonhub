def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    if n >= 3:
        return'YES'
    return 'NO' if arr[0] > arr[1] else 'YES'
if __name__ == '__main__':
    print(solve())