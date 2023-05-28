import sys
from collections import deque
sys.setrecursionlimit(10**8)
input = sys.stdin.readline
n,m,r = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for nodes in graph:
    nodes.sort(reverse=True)
def bfs(start):
    global th, stack
    visited[start] = th
    th += 1
    stack += graph[start]
th = 1
stack = deque([r])
while stack:
    node = stack.popleft()
    if not visited[node]:
        bfs(node)
for v in visited[1:]:
    print(v)