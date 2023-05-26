import sys
from collections import deque
sys.setrecursionlimit(10**9)   

input = sys.stdin.readline
n,m,r = map(int,input().split())
# 간선이 없는 노드(정점)가 있을수도 있기에 for 문으로 tree 맹글어줌
tree, visited = {i:[] for i in range(1,n+1)}, {i:0 for i in range(1,n+1)}
# 양방향 tree 생성
for _ in range(m):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)
# 정점별 노드 내림차순으로 정렬 후 스택으로 변경
for k,v in tree.items():
    tree[k] = deque(sorted(v, reverse=True))
# tree 탐지 함수 생성
cnt = 1
def dfs(node):
    global cnt
    visited[node]=cnt
    while tree[node]:
        tmp_node = tree[node].popleft()
        if (not visited[tmp_node]):
            cnt += 1
            dfs(tmp_node)
dfs(r)
for v in visited.values():
    print(v)