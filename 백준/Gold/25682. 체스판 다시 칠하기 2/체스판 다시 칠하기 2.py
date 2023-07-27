import sys
input = sys.stdin.readline
# 체스판이 첫번째 칸과 같은지 다른지 확인하고 누적합을 생성하는 함수
def check_first(first_block):
    # 정상 체스판의 경우 행열 합이 짝수일 때 첫번째 칸과 같은 색이다.
    prefix_sum = [[0 for _ in range(m+1)] for _ in range(n+1)] # (n+1)*(m+1) 이차원 배열 생성
    for i in range(n):
        for j in range(m):
            if (i + j) % 2 == 0: 
                value = board[i][j] != first_block
            else:
                value = board[i][j] == first_block
            prefix_sum[i+1][j+1] = value + prefix_sum[i+1][j] + prefix_sum[i][j+1] - prefix_sum[i][j]
    cnt = prefix_sum[-1][-1]
    for i in range(1,n-k+2): # n-K+1 ~ n칸까지 포함하여 자르면 k칸짜리 체스판이기에 n-k+2가 끝임
        for j in range(1,m-k+2):  
            tmp = prefix_sum[i+k-1][j+k-1] - prefix_sum[i+k-1][j-1] - prefix_sum[i-1][j+k-1] + prefix_sum[i-1][j-1]
            if cnt > tmp :
                cnt = tmp
    return cnt

n,m,k = map(int,input().split())
board = [list(input().strip()) for _ in range(n)] # ['B','B','B','B'] 형태로 넣어줌
print(min(check_first('W'),check_first('B')))