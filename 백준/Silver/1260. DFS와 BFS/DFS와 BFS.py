import sys
sys.setrecursionlimit(10**8)
from collections import deque
n,m,r = map(int,input().split())
graph = [[] for _ in range(n+1)]
b_visited = [0]*(n+1)
d_visited = [0]*(n+1)
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for nodes in graph:
    nodes.sort()
# bfs
stack = deque([r])
b_ans = []
def bfs(start):
    global bth, stack
    b_visited[start] = 1
    b_ans.append(start)
    stack += graph[start]
while stack:
    node = stack.popleft()
    if not b_visited[node]:
        bfs(node)
# dfs
d_ans = []
def dfs(start):
    d_visited[start] = 1
    d_ans.append(start)
    for node in graph[start]:
        if not d_visited[node]:
            dfs(node)
dfs(r)
print(*d_ans)
print(*b_ans)