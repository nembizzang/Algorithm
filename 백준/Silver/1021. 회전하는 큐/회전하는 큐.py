import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int,input().split())
stack = deque(range(1,n+1)) # stack에 1부터 n까지 넣음
goals = list(map(int,input().split())) # 뽑아내려는 수의 위치
ans = 0
while goals :
    goal = goals.pop(0)
    if stack[0]== goal : # 
        stack.popleft()
    else :
        clock, a_clock = stack.copy(), stack.copy()
        c_rot, a_rot = 0,0
        while clock[0] != goal :
            clock.rotate(1)
            c_rot += 1
        while a_clock[0] != goal :
            a_clock.rotate(-1)
            a_rot += 1
        ans += min(c_rot, a_rot)
        stack = clock if c_rot <= a_rot else a_clock
        stack.popleft()
print(ans)