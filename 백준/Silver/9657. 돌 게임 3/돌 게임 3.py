def solve():
    n = int(input())
    if n % 7 == 0 or n % 7 == 2:
        return 'CY'
    return 'SK'

if __name__ == '__main__':
    print(solve())