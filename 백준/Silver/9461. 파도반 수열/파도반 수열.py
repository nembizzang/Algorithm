import sys
input = sys.stdin.readline
nums = [int(input()) for _ in range(int(input()))]
n = max(nums)
dp = [0]*(n+1)
dp[1],dp[2],dp[3],dp[4],dp[5]=1,1,1,2,2
for i in range(6,n+1):
    dp[i] = dp[i-5] + dp[i-1]
for i in nums:
    print(dp[i])