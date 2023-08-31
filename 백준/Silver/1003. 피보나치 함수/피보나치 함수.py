import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    dp = {i:[] for i in range(n+1)}
    dp[0]=[1,0]
    dp[1]=[0,1]
    for i in range(2,n+1):
        dp[i] = [dp[i-1][j]+dp[i-2][j] for j in range(2)]
    print(*dp[n])