import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)

# dfs 함수 생성
def dfs(row,col):
    if (row==m-1) and (col==n-1) : # 도착했을 경우
        return 1
    
    if dp[row][col] != -1 : # 방문한 적 있을 경우
        return dp[row][col] # 더이상 진행하지 않고 해당 경로에서 가능한 경로 수를 반환
    
    cnt = 0 # 해당 칸에서 도착 가능한 모든 경로의 수를 담는다.
    for i in range(4): # 상하좌우 이동
        nrow,ncol = row+drow[i], col+dcol[i] # 이동할 칸 초기화
        if 0<=nrow<m and 0<=ncol<n and maps[row][col] > maps[nrow][ncol]: # 이동가능하면
            cnt += dfs(nrow,ncol) # dfs 진행한 결과 중 도착 가능한 수를 담음
    dp[row][col] = cnt
    return dp[row][col] # 해당 칸에서 모든 확인이 끝났다면 해당 칸에서 도착 가능한 경로 수를 반환

m,n = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(m)]
dp = [[-1]*n for _ in range(m)] # 0으로 해주면 도착 가능 경로 수가 0회인 곳과 미방문 지역을 구분 불가
drow,dcol = [-1,1,0,0], [0,0,-1,1]
print(dfs(0,0))