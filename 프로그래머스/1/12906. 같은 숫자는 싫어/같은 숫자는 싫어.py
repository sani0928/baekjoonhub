def solution(arr):
    answer = [arr[0]]
    cur = arr[0]
    for n in arr[1:]:
        if cur == n: continue
        answer.append(n)
        cur = n
    return answer