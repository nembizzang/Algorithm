from itertools import combinations_with_replacement as cwr
n,m = map(int,open(0).read().split())
for combi in cwr(range(1,n+1),m):
    print(*combi)