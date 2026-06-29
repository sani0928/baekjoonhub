from math import lcm

def solution(signals):

    limit = 1
    for g, y, r in signals:
        limit = lcm(limit, g + y + r)
    
    for time in range(1, limit + 1):
        all_yellow = True
        for g, y, r in signals:
            pos = (time - 1) % (g + y + r)
            
            if not (g <= pos < g + y):
                all_yellow = False
                break
                
        if all_yellow:
            return time
                
    return -1