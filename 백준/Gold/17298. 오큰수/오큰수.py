import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))
ans = [-1]*n
stack = [] # 오큰수를 찾아야하는 nums의 인덱스를 담아준다.

for i in range(n):
    # stack이 있고, 오큰수를 찾아야하는 수보다 더 큰 수가 나타났다. => 오큰수를 발견했다.
    while stack and nums[stack[-1]] < nums[i] :
        ans[stack.pop()] = nums[i] # 오큰수를 발견한 인덱스는 pop으로 빼내준다.
    stack.append(i) # 이때 i는 오큰수가 되는 인덱스기에 이 인덱스에 대한 오큰수도 찾아줘야한다.
print(*ans)