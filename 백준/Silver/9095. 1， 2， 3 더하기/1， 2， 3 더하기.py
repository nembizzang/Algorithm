import sys
input = sys.stdin.readline
dp = {0:1,1:1,2:2}
for i in range(3,12):
    dp[i]=dp[i-3]+dp[i-2]+dp[i-1]
for _ in range(int(input())):
    print(dp[int(input())])