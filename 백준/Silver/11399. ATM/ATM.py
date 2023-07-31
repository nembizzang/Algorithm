import sys
input = sys.stdin.readline
n = int(input())
# 빨리 인출하는 사람이 먼저 뽑고 나가야 뒤에서 덜 기다림
times = sorted(list(map(int,input().split()))) # 시간 순으로 정렬
waiting = [] # 재정렬한 순서대로 뽑았을 때 순서별 대기시간
tmp_time = 0 # 현재 사람의 대기시간
# 누적합 구하기
for time in times :
    tmp_time += time
    waiting.append(tmp_time)
print(sum(waiting))