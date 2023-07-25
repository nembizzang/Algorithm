import sys
input = sys.stdin.readline
n,m = map(int, input().split())
nums = list(map(int, input().split()))

# 첫번째 숫자부터 i번째 숫자까지의 합으로 구성된 배열(1<=i<=n)
prefix_sum =[0]
tmp_sum = 0
for num in nums:
    tmp_sum += num
    prefix_sum.append(tmp_sum)

for _ in range(m):
    sta, end = map(int,input().split())
    print(prefix_sum[end]-prefix_sum[sta-1]) # end번째까지의 합 - (sta-1)번째까지의 합