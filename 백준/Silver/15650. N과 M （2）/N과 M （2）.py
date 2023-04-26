from itertools import combinations
n,m = map(int,open(0).read().split())
for combi in combinations(range(1,n+1),m):
    print(*combi)