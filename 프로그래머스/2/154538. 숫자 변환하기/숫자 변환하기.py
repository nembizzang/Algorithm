'''
연산회수를 하나씩 늘려가며 제일 먼저 도착하는 경우에 바로 return할 수 있도록
heap을 포함한 bfs를 활용하자.
이때 곱하기 연산은 수가 빨리 커지고 확인할 수의 간격이 넓어지므로 비효율적이기에
출발과 도착 지점을 바꾸어 나누기 연산으로 진행
'''
from heapq import heappush, heappop
def solution(x, y, n):
    visited = [-1]*(y+1)
    stack = []
    heappush(stack,[0,y]) # 연산 횟수, 출발 지점(가장 적은 횟수로 x에 가깝게 간 것부터 bfs 진행)
    while stack:
        cnt, num = heappop(stack)
        if num == x: # 도착했다면
            return cnt
        if num < x: # 연산횟수 초과 시 탐색 중지
            continue
        if visited[num]==-1 or visited[num]>cnt: # 최초 방문이거나 더 빠르게 방문한 경우에만 진행
            visited[num] = cnt # 방문 경험 초기화
            cnt += 1 # 연산 횟수 추가
            if num%3 == 0:
                heappush(stack,[cnt,num//3])
            if num%2 == 0:
                heappush(stack,[cnt,num//2])
            heappush(stack,[cnt,num-n])
    return -1 # 도달 못하는 경우