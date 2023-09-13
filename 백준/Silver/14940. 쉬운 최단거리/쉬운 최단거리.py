import sys
from collections import deque
input = sys.stdin.readline

def bfs(y,x):
    stack = deque([[y,x]])
    while stack :
        y,x = stack.popleft()
        for i in range(4):
            ny,nx = y+dy[i],x+dx[i]
            if 0<=ny<n and 0<=nx<m and maps[ny][nx] and visited[ny][nx]>visited[y][x]+1:
                visited[ny][nx] = visited[y][x]+1
                stack.append([ny,nx])
n,m = map(int,input().split())
maps = []
goal = []
for i in range(n):
    row = list(map(int,input().split()))
    maps.append(row)
    if 2 in row :
        goal += [i,row.index(2)]
visited = [[n*m]*m for _ in range(n)]
visited[goal[0]][goal[1]]=0
dy,dx = [-1,1,0,0],[0,0,-1,1]
bfs(*goal)
for i in range(n):
    row = visited[i]
    for j,num in enumerate(row):
        if num == n*m : # 가지 못한 곳
            row[j] = 0 if not maps[i][j] else -1 # 벽이면 0 아니면 -1   
    print(*row)