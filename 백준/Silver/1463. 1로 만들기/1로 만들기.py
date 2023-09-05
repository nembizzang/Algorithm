import sys
from collections import defaultdict, deque
input = sys.stdin.readline
def bfs(n):
    stack = deque([[n,0]])
    cnt = 0
    while stack:
        i,cnt = stack.popleft()
        if i==1:
            return cnt
        cnt += 1
        if (not i%3) and (i>=3) and (not dp[i//3]):
            stack.append([i//3,cnt])
            dp[i%3] = 1
        if (not i%2) and (i>=2) and (not dp[i//2]):
            stack.append([i//2,cnt])
            dp[i%2] = 1
        if (not dp[i-1]):
            stack.append([i-1,cnt])
            dp[i-1] = 1
n = int(input())
dp = defaultdict(int)
print(bfs(n))