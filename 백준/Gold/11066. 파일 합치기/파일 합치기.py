import sys
input = sys.stdin.readline
# 누적합 구하는 함수
def prefix(chaps):
    sum_prefix = [0]
    tmp_sum = 0
    for chap in chaps:
        tmp_sum += chap
        sum_prefix.append(tmp_sum)
    return sum_prefix
# dp 함수
def make_dp(a,b):
    dp[a][b] = min([dp[a][a+i] + dp[a+i+1][b] for i in range(b-a)]) + sum_prefix[b]-sum_prefix[a-1]
for _ in range(int(input())):
    k = int(input())
    chaps = list(map(int,input().split()))
    # 누적합 구하기
    sum_prefix = prefix(chaps)
    # dp 채워넣기
    dp = [[0]*(k+1) for _ in range(k+1)]
    for d in range(1,k):
        for i in range(1,k):
            if i+d <= k:
                make_dp(i,i+d)

    print(dp[1][k])