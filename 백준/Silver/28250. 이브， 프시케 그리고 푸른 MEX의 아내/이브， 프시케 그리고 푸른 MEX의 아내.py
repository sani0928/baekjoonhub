'''
각 조합이 나오는 횟수
- {0, 0}은 cnt_0 * (cnt_0 - 1) // 2
- {0, rest = 0과 1를 제외한 나머지}은 cnt_0 * rest
- {0, 1}은 cnt_0 * cnt_1
mex({0, 0})과 mex({0, rest})는 +1, mex({0, 1}))는 +2
'''
n = int(input())
arr = list(map(int, input().split()))
cnt_0 = arr.count(0)
cnt_1 = arr.count(1)
rest = n - cnt_0 - cnt_1
print(cnt_0 * (cnt_0 - 1) // 2 + cnt_0 * rest + 2 * cnt_0 * cnt_1)