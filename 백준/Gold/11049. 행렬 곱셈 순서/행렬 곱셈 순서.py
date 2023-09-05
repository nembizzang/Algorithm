import sys
input = sys.stdin.readline
n = int(input())
nums = [[0,0]]+[list(map(int,input().split())) for _ in range(n)]
dp = [[0]*(n+1) for _ in range(n+1)]
for i in range(1,n): # 간격
    for j in range(1,n-i+1): # 시작점
        s,e = j,j+i
        tmp = nums[s][0]*nums[e][1]
        dp[s][e] = min([dp[s][k] + dp[k+1][e] + tmp*nums[k][1] for k in range(s,e)])
print(dp[1][n])
# n=4일때, dp 순환
# [1,2] / [2,3] / [3,4]
# [1,3] / [2,4]
# [1,4]
# i=1 : j는 1~3까지 / j=1 : dp[1][2] / j=2 : dp[2][3] / j=3 : dp[3][4]
# i=2 : j는 1~2까지 / j=1 : dp[1][3] / j=2 : dp[2][4]
# i=3 : j는 1~1까지 / j=1 : dp[1][4]