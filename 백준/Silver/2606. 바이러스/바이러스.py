import sys
input = sys.stdin.readline

n = int(input())
t = int(input())

dic = {}

for i in range(n) :
  dic[i+1] = []

for i in range(t) :
  a,b = map(int, input().split())
  dic[a].append(b)
  dic[b].append(a)

def dfs(dic, start) :
  for i in dic[start] :
    if i not in visited:
      visited.append(i)
      dfs(dic,i)

visited = [1]
dfs(dic,1)
print(len(visited)-1)