from math import ceil
h, w, n, m = map(int, input().split())
h_cnt = ceil(h / (n + 1))
w_cnt = ceil(w / (m + 1))
print(h_cnt * w_cnt)