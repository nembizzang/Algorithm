import sys
input = sys.stdin.readline
# 1차로 시작 시간 순으로 정렬
meetings = sorted([list(map(int,input().split())) for _ in range(int(input()))])
# 2차로 종료 시간 순으로 정렬
meetings.sort(key=lambda x : x[1])
# 회의 개수와 최종 회의 종료 시간
cnt = last = 0
for sta,end in meetings:
    if last <= sta : # 최종 회의 시간 종료 이후 다음 회의가 시작이라면
        cnt += 1 # 회의가 가능하므로 +1
        last = end # 최종 회의 종료 시간 초기화
print(cnt)