import sys
input = sys.stdin.readline
n,m = map(int,input().split())
no_listen = set([input().strip() for _ in range(n)])
no_see = set([input().strip() for _ in range(m)])
no_listen_see = no_listen & no_see
print(len(no_listen_see))
for i in sorted(no_listen_see):
    print(i)