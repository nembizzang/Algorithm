import sys
input = sys.stdin.readline
n,m = map(int,input().split())
memories = list(map(int,input().split()))
costs = list(map(int,input().split()))
dp = [[0]*(sum(costs)+1) for _ in range(n)]
ans = sum(costs)
# dp[i][j] = i번째 App까지 확인했을 때 j 코스트 이상에서 얻을 수 있는 최고의 메모리
for i in range(n):
    byte, cost = memories[i], costs[i] # 확인할 app의 byte와 cost가져오기
    for j in range(sum(costs)+1):
        if cost > j : # 해당 app 비활성화 cost가 확인하는 cost보다 높다면
            dp[i][j] = dp[i-1][j] # 위의 행 결과(이전 app까지 확 인결과) 가져오기
        else : # 해당 app 비활성화가 가능한 cost라면
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-cost]+byte) # 이전 행 결과와 앞선 app 확인 결과 중 해당 app cost가 가능한 경우 중 최댓값
        if (dp[i][j] >= m) & (j < ans) : # dp[i][j]가 최소 메모리 기준을 만족하고 cost가 최소라면
            ans = j
print(ans) # 모든 dp를 채우고나서 답을 반환  