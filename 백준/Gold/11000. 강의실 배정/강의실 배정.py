import sys
input = sys.stdin.readline

data = []
n = int(input())
for _ in range(n):
    s, t = map(int, input().split())
    data.append((s, 1))
    data.append((t, -1))
data.sort(key=lambda x: (x[0], x[1])) # 시간순 정렬
mx = cur = 0
for _, what in data:
    cur += what # 진행 중인 강의실 누적합 반영
    mx = max(mx, cur) # 동시에 진행 중인 강의수 최댓값 갱신
print(mx)