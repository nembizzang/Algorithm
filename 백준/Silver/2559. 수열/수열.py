import sys
from collections import deque
input = sys.stdin.readline
n,k = map(int,input().split())
temps = list(map(int,input().split()))
# 시간복잡도를 줄이기 위해 stack 사용
left, right = deque(temps[:k]), deque(temps[k:])

# 1일~k일까지 온도의 합
ans = k_sum = sum(left)

# right에 남은 숫자가 없을 때까지 right의 왼쪽에서 숫자 하나씩 빼줄거임
while right :
    new_num = right.popleft() # right에서 왼쪽에서 숫자 빼서
    left.append(new_num) # left의 오른쪽에 넣어줌
    k_sum += new_num - left.popleft() # 현재 합을 변경
    if ans < k_sum:
        ans = k_sum # 그 합이 ans보다 크면 ans 최신화
print(ans)