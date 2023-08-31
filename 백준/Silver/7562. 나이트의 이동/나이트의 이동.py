import sys
from collections import deque
input = sys.stdin.readline

def bfs(sta_y,sta_x): # 최초 위치(x,y)를 넣고 최소이동횟수를 반환하는 bfs 생성
    stack = deque([[sta_y,sta_x,0]])
    while stack :
        cur_y,cur_x,cnt = stack.popleft() # stack에서 현재 위치(x,y)와 이동횟수를 뽑아낸다.
        if [cur_y,cur_x] == [end_y,end_x]: # 도착했다면
            return cnt # 정답출력(이동횟수 오름차순으로 bfs이므로 처음 출력되는 값이 최소값이다)
        cnt += 1 # 현재 이동횟수 1 추가
        for i in range(8): # 나이트가 갈 수 있는 8개의 방향
            ny,nx = cur_y+dy[i], cur_x+dx[i]
            if (0<=ny<l) and (0<=nx<l) and (chk[ny][nx]==0): # 보드 위에 있고 처음가는 곳이라면
                stack.append([ny,nx,cnt]) # stack에 추가
                chk[ny][nx] = 1 # chk에 방문경험 초기화

dy = [-1,-2,-2,-1,1,2,2,1]
dx = [-2,-1,1,2,2,1,-1,-2]     
for _ in range(int(input())):
    l = int(input())
    sta_y, sta_x = map(int,input().split())
    end_y, end_x = map(int,input().split())
    chk = [[0]*l for _ in range(l)]
    print(bfs(sta_y,sta_x))