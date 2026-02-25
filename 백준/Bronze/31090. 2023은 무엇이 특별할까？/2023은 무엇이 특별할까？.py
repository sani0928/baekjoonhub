t = int(input())
while t > 0:
    n = int(input())
    n2 = n + 1
    n = int(str(n).strip()[2:])
    if n2 % n == 0:
        print('Good')
    else:
        print('Bye')
    t -=  1