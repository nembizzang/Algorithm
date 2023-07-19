import sys
input = sys.stdin.readline
R=G=B=0
for _ in range(int(input())):
    r,g,b = map(int,input().split())
    R,G,B = r+min(G,B), g+min(R,B), b+min(R,G)
print(min(R,G,B))