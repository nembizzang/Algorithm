import sys
from collections import deque, defaultdict
input = sys.stdin.readline
def bfs(i):
    stack = deque([i])
    while stack:
        for j in dic[stack.popleft()]:
            if not visited[j] : # 방문한 적이 없다면
                visited[j]=1 # 방문표시
                stack.append(j)
    return sum(visited.values())

n = int(input())
dic = defaultdict(list)
for _ in range(int(input())):
    a,b = map(int,input().split())
    dic[a].append(b)
    dic[b].append(a)
    
visited = {i:0 for i in range(1,n+1)}
visited[1] = 1
print(bfs(1)-1)