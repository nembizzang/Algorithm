from itertools import product
n,m = map(int,open(0).read().split())
for prod in product(range(1,n+1),repeat=m):
    print(*prod)