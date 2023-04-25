import sys
from collections import deque
input = sys.stdin.readline
stack = deque(range(1,int(input())+1))

# 1) len(stack) 사용
#while len(stack)>1:
#    stack.popleft()
#    stack.append(stack.popleft())
#print(stack.popleft())

# 2) try-except 사용
while True:
    x = stack.popleft()
    try:
        stack.append(stack.popleft())
    except:
        print(x)
        break