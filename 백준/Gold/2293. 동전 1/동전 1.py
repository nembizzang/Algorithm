import sys
input = sys.stdin.readline

n,k = map(int,input().split())
coins = [int(input()) for _ in range(n)]
dp = [0]*(k+1)
dp[0] = 1 # 0으로 0을 만드는 방법 1가지 추가, 이걸 지정해줘야 첫번째 동전이 들어올 때 가지수 추가 가능
for coin in coins : # 동전을 한 종류씩 꺼내서
    for i in range(coin,k+1): # 해당 동전이 추가될 수 있는 가치의 범위(해당 동전 가치~k)
        dp[i] += dp[i-coin]
print(dp[-1])