import sys
from heapq import heappop
input = sys.stdin.readline

def bfs():
    heap = [[1,0,0,0]]
    while heap :
        cnt,y,x,crashed = heappop(heap)
        if y==n-1 and x==m-1 : # 도착했다면 반환
            return cnt # 도착 칸 수
        cnt += 1
        if 0<y and not visited[y-1][x][crashed]: # 이동 가능하고 최초 방문이라면
            if maps[y-1][x] == 1 and not crashed :# 벽이고 부순 적이 없다면
                visited[y-1][x][1] = 1 # 벽 부수고 방문
                heap.append([cnt,y-1,x,1]) # 이동칸수,y,x,crashed heap에 넣기
            elif not maps[y-1][x] : # 벽이 아니라면
                visited[y-1][x][crashed] = 1 # 벽 안부수고 방문
                heap.append([cnt,y-1,x,crashed]) # 이동칸수,y,x,crashed heap에 넣기
        if y<n-1 and not visited[y+1][x][crashed] : # 이동 가능하고 최초 방문이라면
            if maps[y+1][x] == 1 and not crashed :# 벽이고 부순 적이 없다면
                visited[y+1][x][1] = 1 # 벽 부수고 방문
                heap.append([cnt,y+1,x,1]) # 이동칸수,y,x,crashed heap에 넣기
            elif not maps[y+1][x] : # 벽이 아니라면
                visited[y+1][x][crashed] = 1 # 벽 안부수고 방문
                heap.append([cnt,y+1,x,crashed]) # 이동칸수,y,x,crashed heap에 넣기
        if 0<x and not visited[y][x-1][crashed] : # 이동 가능하고 최초 방문이라면
            if maps[y][x-1] == 1 and not crashed :# 벽이고 부순 적이 없다면
                visited[y][x-1][1] = 1 # 벽 부수고 방문
                heap.append([cnt,y,x-1,1]) # 이동칸수,y,x,crashed heap에 넣기
            elif not maps[y][x-1] : # 벽이 아니라면
                visited[y][x-1][crashed] = 1 # 벽 안부수고 방문
                heap.append([cnt,y,x-1,crashed]) # 이동칸수,y,x,crashed heap에 넣기
        if x<m-1 and not visited[y][x+1][crashed] : # 이동 가능하고 최초 방문이라면
            if maps[y][x+1] == 1 and not crashed :# 벽이고 부순 적이 없다면
                visited[y][x+1][1] = 1 # 벽 부수고 방문
                heap.append([cnt,y,x+1,1]) # 이동칸수,y,x,crashed heap에 넣기
            elif not maps[y][x+1] : # 벽이 아니라면
                visited[y][x+1][crashed] = 1 # 벽 안부수고 방문
                heap.append([cnt,y,x+1,crashed]) # 이동칸수,y,x,crashed heap에 넣기
    return -1

n,m = map(int,input().split())
maps = [list(map(int,list(input().strip()))) for _ in range(n)]
visited = [[[0]*2 for _ in range(m)] for _ in range(n)] # [y][x][0]은 안뚫 방문 [y][x][1]은 벽뚫방문
visited[0][0][0]=1 # 첫번째 칸 방문 이력 추가
print(bfs())