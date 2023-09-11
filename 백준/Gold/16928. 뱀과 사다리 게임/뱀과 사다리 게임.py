import sys
from heapq import heappush, heappop
input = sys.stdin.readline

def bfs():
    heap = [[0,1]] # 0회 이동, 출발점은 1번
    while heap :
        cnt, tmp = heappop(heap) # 현 위치, 이동 횟수
        cnt += 1 # 이동 횟수 증가
        for i in range(1,7): # 주사위 굴리기
            if tmp+i <= 100 : # 이동 가능하다면
                new = mov[tmp+i] # 새로운 곳으로 이동
                if visited[new] > cnt : # 현재 기록된 최소 방문 횟수보다 작다면
                    visited[new] = cnt # 최소 방문 횟수 초기화
                    if new == 100 : # 도착 했다면
                        return cnt
                    heap.append([cnt,new]) # 새롭게 이동
n,m = map(int,input().split())
mov,visited = {},{} # 이동하는 칸(뱀,사다리), 해당 칸 최소 방문 횟수
for i in range(1,101):
    mov[i], visited[i] = i,100 # 100번째 칸까지 최대 이동 횟수는 99이므로
for _ in range(n+m):
    sta,end = map(int,input().split())
    mov[sta] = end
print(bfs())