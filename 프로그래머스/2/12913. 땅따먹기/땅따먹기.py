'''
i행 j열 칸까지 도달할 때까지의 최대값은 다음과 같은 점화식으로 나타낼 수 있다.
dp[i][j] = land[i][j]+max(dp[i-1][:j]+dp[i-1][j+1:])
위와 같은 점화식으로 마지막 행에 도착했을 때의 최대값을 구하자.
'''
def solution(land):
    dp = [[0]*len(land[0]) for _ in range(len(land)+1)]
    for i in range(1,len(land)+1): # 행 순회
        for j in range(len(land[0])): # 열 순회
            dp[i][j] = land[i-1][j]+max(dp[i-1][:j]+dp[i-1][j+1:]) # land가 dp보다 인덱스가 하나씩 적으므로
    return max(dp[-1])