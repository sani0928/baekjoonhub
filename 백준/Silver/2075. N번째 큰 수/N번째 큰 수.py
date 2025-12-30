import heapq

N = int(input())
hq = []
for _ in range(N):
    max_num = 0
    for num in map(int, input().split()):
        # hq엔 N개만 저장
        if len(hq) < N:
            heapq.heappush(hq, num)
            continue
        # 현재 hq의 최솟값보다 크면 교체
        if num > hq[0]:
            heapq.heapreplace(hq, num)
print(hq[0])