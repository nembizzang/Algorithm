import sys
from collections import deque
input = sys.stdin.readline
# bfs 생성
def bfs(): # 익은 토마토 위치(y행, x열)로부터 다음날 익게되는 토마토 위치 추가
    global stack, not_good
    cnt = 0 # 최초 날짜
    while stack:
        y,x,cur = stack.popleft()
        if cur!=cnt : # 날이 넘어갔으면 토마토 확인
            if not not_good : # 모든 토마토가 익었다면
                return cur # 다 익은 날 출력
            else : # 다 익지 않았다면
                cnt += 1 # 날짜 하루 경과
        cur += 1 # 다음번 bfs로 넣을 때는 다음 날짜로 진행
        for i in range(4):
            ny,nx = y+dy[i],x+dx[i]
            if 0<=ny<n and 0<=nx<m and tomato[ny][nx]==0 : # 이동가능하고 안익은 토마토라면
                tomato[ny][nx] = 1 # 익은 토마토 추가
                not_good -= 1
                stack.append([ny,nx,cur]) # 익은 토마토 bfs 추가
    return -1 # 안 익은 토마토가 있지만 stack이 끝난다면 다 익는게 불가능이므로 -1 출력
m,n = map(int,input().split())
tomato = []
stack = deque()
not_good = 0 # 전체 개수, 안 익은 개수
dy,dx = [-1,1,0,0],[0,0,-1,1]
for i in range(n):
    row = list(map(int,input().split()))
    for j in range(m):
        if row[j]==1: # i행 j열에 익은 토마토가 있다면
            stack.append([i,j,0]) # stack에 토마토 위치, 현재날짜(0) 추가
        elif row[j]==0: # 안 익은 토마토가 있다면
            not_good += 1 # 안 익은 토마토 개수 추가
    tomato.append(row)
if not not_good: # 안 익은 토마토가 없다면
    print(0)
else : # 안 익은 토마토가 있다면
    print(bfs()) # bfs 진행