import sys
input = sys.stdin.readline
n,m = map(int, input().split())
nums = []
for _ in range(n):
    nums.append(list(map(int,input().split()))) # 전체 2차원 배열 생성
# 누적합을 넣을 (n+1)*(n+1) 배열 생성
sum_num = [[0 for _ in range(n+1)] for _ in range(n+1)]
for row in range(1,n+1):
    for col in range(1,n+1):
        sum_num[row][col] = nums[row-1][col-1] + sum_num[row-1][col] + sum_num[row][col-1] - sum_num[row-1][col-1]
for _ in range(m):
    x1,y1,x2,y2 = map(int, input().split())
    ans = sum_num[x2][y2] - sum_num[x2][y1-1] - sum_num[x1-1][y2] + sum_num[x1-1][y1-1]
    print(ans)