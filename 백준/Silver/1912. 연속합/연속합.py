import sys
input = sys.stdin.readline
n = int(input())
nums = list(map(int,input().split()))
dp = [0]*(n) # dp[n-1]은 nums[:n]에서 n번째 원소를 포함하는 연속합중 최대값
dp[0]=nums[0]
for i in range(1,n):
    dp[i] = max(dp[i-1]+nums[i],nums[i])
# nums = 10 -4 3  1  5  6 -35 12 21 -1
# dp =   10  6 9 10 15 21 -14 12 33 32
print(max(dp))