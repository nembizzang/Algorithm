import sys
input = sys.stdin.readline
n,k = map(int, input().split())
dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
stuff = [map(int, input().split()) for _ in range(n)]
for i in range(n):
    w,v = stuff[i]
    for j in range(1,k+1):
        if j<w :
            dp[i+1][j] = dp[i][j]
        else :
            dp[i+1][j] = max(dp[i][j-w]+v, dp[i][j])
print(dp[n][k])