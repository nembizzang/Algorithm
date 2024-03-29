import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int,input().split())
maze = [list(map(int,input().strip())) for _ in range(n)]
# 해당 칸으로 진행 가능한지, 진행하면 최소로 진행한 거리인지 확인하는 함수
def bfs(row,col,cnt):
    stack = deque()
    stack.append([row,col,cnt])
    while stack :
        row,col,cnt = stack.popleft()
        if (row==n-1)&(col==m-1): # 최초로 마지막 칸에 도착했다면
            return(cnt)
        for d_row,d_col in [[-1,0],[1,0],[0,-1],[0,1]] : # 상하좌우 이동으로 도착할 다음 칸
            n_row, n_col = row+d_row, col+d_col # 이동하려는 칸 초기화
            if (0<=n_row<n) & (0<=n_col<m) : # 새로 이동하는 칸이 maze 내 범위이고
                if maze[n_row][n_col] == 1 : # 이번 칸이 처음 이동하는 칸이라면
                    stack.append([n_row,n_col,cnt+1]) # 이동하는 칸에서 또 확인
                    maze[n_row][n_col] = cnt+1 # 다음번 도착하는 칸 초기화
print(bfs(0,0,1)) # 이번 행, 이번 열, 이번 칸 도착 시 밟은 칸 수