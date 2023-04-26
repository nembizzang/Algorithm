import sys
from collections import deque
input = sys.stdin.readline
stack = deque([])
for _ in range(int(input())):
    order = input().split()
    if order[0] == 'push_front' :
        stack.appendleft(order[1])
    elif order[0] == 'push_back':
        stack.append(order[1])
    elif order[0] == 'pop_front':
        print(stack.popleft() if stack else -1)
    elif order[0] == 'pop_back':
        print(stack.pop() if stack else -1)
    elif order[0] == 'size':
        print(len(stack))
    elif order[0] == 'empty':
        print(0 if stack else 1)
    elif order[0] == 'front':
        print(stack[0] if stack else -1)
    else :
        print(stack[-1] if stack else -1)