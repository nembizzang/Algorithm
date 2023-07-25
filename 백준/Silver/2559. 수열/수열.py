import sys
from collections import deque
input = sys.stdin.readline
n,k = map(int,input().split())
temps = list(map(int,input().split()))
# 시간복잡도를 줄이기 위해 stack 사용
left, right = deque(temps[:k]), deque(temps[k:])
# 1일~k일까지 온도의 합
ans = k_sum = sum(left)
while right :
    new_num = right.popleft()
    left.append(new_num)
    k_sum += new_num - left.popleft()
    if ans < k_sum:
        ans = k_sum
print(ans)