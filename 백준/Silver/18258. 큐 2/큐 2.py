import sys
input = sys.stdin.readline
from collections import deque
stack = deque([])

for _ in range(int(input())):
    x = input().split()
    if x[0] == 'push':
        stack.append(x[1])
    elif x[0] == 'pop':
        try : print(stack.popleft())
        except : print(-1)
    elif x[0] == 'size':
        try : print(len(stack))
        except : print(0)
    elif x[0] == 'empty':
        print(0 if stack else 1)
    elif x[0] == 'front':
        try : print(stack[0])
        except : print(-1)
    else:
        try : print(stack[-1])
        except : print(-1)