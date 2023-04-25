from collections import deque
n,k = map(int,open(0).read().split())
stack = deque(range(1,n+1))
ans = '<'
while stack:
    # 빠진 사람 자리로 땡겨진 사람에게로 포인터가 맞춰져있으므로 한칸 덜 회전 + 시작은 -1번째 사람부터 해야맞음
    stack.rotate(-k+1) 
    ans += str(stack.popleft())
    ans += ', ' if stack else '>'
print(ans)