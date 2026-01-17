x, y, w, s = map(int, input().split())
gap = abs(x - y)
# 단순 보도 이동
candi1 = (x + y) * w
# 가능한 만큼 대각선 이동 후 2칸 단위로 나누어 대각선 보도 중 더 짧은 거리 선택 (홀수면 1칸 보도 이동)
candi2 = min(x, y) * s + (gap // 2) * min(2 * w, 2 * s) + (gap % 2) * w
# 대각선으로만 이동 (gap이 홀수면 한칸은 보도 이동)
candi3 = max(x, y) * s if gap % 2 == 0 else (max(x, y) - 1) * s + w
print(min(candi1, candi2, candi3))