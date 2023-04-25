from itertools import permutations
n,m = map(int, open(0).read().split())
for combi in list(permutations(range(1,n+1),m)):
    print(*combi)