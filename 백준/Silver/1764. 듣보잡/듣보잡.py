import sys
input = sys.stdin.readline

n,m = map(int,input().split())

nl = {}
ans = []
ans_n = 0
for _ in range(n):
    name = input().strip()
    nl[name] = name
for _ in range(m):
    try :
        ans.append(nl[input().strip()])
        ans_n += 1
    except :
        pass
print(ans_n)
for i in sorted(ans):
    print(i)