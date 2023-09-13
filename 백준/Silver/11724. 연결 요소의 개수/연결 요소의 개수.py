import sys
input = sys.stdin.readline

def find(x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parents[x] != x:
        parents[x] = find(parents[x]) # 재귀 함수를 돌며
        return parents[x]
    return x

def union(a,b):
    a,b = find(a), find(b)
    if a<b :
        parents[b] = a
    else :
        parents[a] = b
        
n,m = map(int,input().split()) # 노드 개수, 간선 개수
nodes = range(1,n+1)
parents = [i for i in range(n+1)] # 자기 자신을 부모 노드로 초기화
for _ in range(m):
    a,b = map(int,input().split())
    union(a,b)

for node in nodes:
    find(node)
print(len(set(parents))-1)