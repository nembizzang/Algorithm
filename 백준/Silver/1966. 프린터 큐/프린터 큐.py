import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    n,m = map(int,input().split())
    importances = deque(map(int,input().split()))
    out = max(importances) # 중요도 가장 높은 것
    cnt = 1 # 인쇄 횟수
    while True:
        cur = importances.popleft()         # 이번 출력물 중요도
        if out != cur:                      # 이번 출력물이 중요도 가장 높은 것이 아니라면
            importances.append(cur)         # 출력 못하고 중요도(출력순서) 맨 뒤로
            if not m :                      # 확인할 거가 출력할 차례였다면
                m = len(importances)-1      # 확인할 거 출력순서 맨 끝
            else :                          # 출력할 차례가 아니었다.
                m -= 1                      # 출력 순서 한 칸 땡기기
        else :                              # 이번 출력물이 중요도 가장 높은 것이라면
            if not m :                      # 확인할거가 출력할 차례였다면
                print(cnt)                  # 그대로 인쇄횟수 출력
                break                       # 다음 테케로 진행시켜
            else :                          # 이번 출력물이 중요도 가장 높은게 아니라면
                m -= 1                      # 확인할거 순서 -1
                cnt += 1                    # 출력횟수 +1
                out = max(importances)      # 중요도 맥스 재설정