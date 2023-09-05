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
        if (not i%3)and (not visited[i//3]):
            stack.append([i//3,cnt])
            visited[i%3] = 1
        if (not i%2)and (not visited[i//2]):
            stack.append([i//2,cnt])
            visited[i%2] = 1
        if (not visited[i-1]):
            stack.append([i-1,cnt])
            visited[i-1] = 1
n = int(input())
visited = defaultdict(int)
print(bfs(n))