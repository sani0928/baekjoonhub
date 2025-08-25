import sys

input = sys.stdin.readline

T = int(input())

for tc in range(T):

    N = int(input())
    ans = 0
    interviewee = [tuple(map(int, input().split())) for _ in range(N)]
    interviewee.sort()
    # 서류순으로 오름차순, 서류 1등은 무조건 합격
    # 면접 등수로만 판별 가능
    best = 100**9
    for _, interview_score in interviewee:
        if interview_score < best:
            # 현재 최고 등수보다 낮다면 통과
            ans += 1
            best = interview_score
    print(ans)