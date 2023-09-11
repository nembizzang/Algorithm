import sys
from collections import deque
input = sys.stdin.readline

def bfs() : # 0일자부터 토마토 익히기 시작
    global not_good
    cur_day = 0 # 현재 날짜
    while stack :
        z,y,x,chk_day = stack.popleft()
        if cur_day != chk_day : # 날짜가 넘어갔다면
            if not not_good : # 전부 익었다면
                return chk_day # 전부 익은 날짜 반환
            cur_day += 1 # 현재 날짜 하루 더 진행
        chk_day += 1 # 확인할 날짜 하루 더 진행
        if (0<z) and (not tomatoes[z-1][y][x]):
            tomatoes[z-1][y][x] = 1
            stack.append([z-1,y,x,chk_day])
            not_good -= 1
        if (z<(h-1)) and (not tomatoes[z+1][y][x]) :
            tomatoes[z+1][y][x] = 1
            stack.append([z+1,y,x,chk_day])
            not_good -= 1
        if (0<y) and (not tomatoes[z][y-1][x]) :
            tomatoes[z][y-1][x] = 1
            stack.append([z,y-1,x,chk_day])
            not_good -= 1
        if (y<(n-1)) and (not tomatoes[z][y+1][x]) :
            tomatoes[z][y+1][x] = 1
            stack.append([z,y+1,x,chk_day])
            not_good -= 1
        if (0<x) and (not tomatoes[z][y][x-1]) :
            tomatoes[z][y][x-1] = 1
            stack.append([z,y,x-1,chk_day])
            not_good -= 1
        if (x<(m-1)) and (not tomatoes[z][y][x+1]) :
            tomatoes[z][y][x+1] = 1
            stack.append([z,y,x+1,chk_day])
            not_good -= 1
    return -1

m,n,h = map(int,input().split())
not_good = 0 # 안 익은 개수
stack = deque([]) # bfs 넣을 stack
tomatoes = [] # 전체 상자
for z in range(h): # 층(z) 반복
    floor = []
    for y in range(n): # 행(y) 반복
        row = list(map(int,input().split()))
        for x,tom in enumerate(row): # 열(x) 반복
            if tom == 1: # 익었다면
                stack.append([z,y,x,0]) # bfs에 먼저 넣어두기, 0은 일자
            elif tom == 0 : # 안 익었다면
                not_good += 1 # 안 익은 개수 추가
        floor.append(row) # 층에 행 넣기
    tomatoes.append(floor) # 전체 상자에 층 넣기
dx,dy,dz = [0,0,-1,1,0,0],[-1,1,0,0,0,0],[0,0,0,0,-1,1] # 상하좌우위아래 방향
if not not_good : # 애초에 안익은 토마토가 없다면
    print(0)
else :
    print(bfs())