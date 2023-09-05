import sys
input = sys.stdin.readline
n,m = list(map(int,input().split()))

dic = {}
for i in range(1,n+1) :
    name = input().strip()
    dic[str(i)] = name
    dic[name] = str(i)
    
for _ in range(m) :
    print(dic[input().strip()])