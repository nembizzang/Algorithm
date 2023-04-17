a,b,c = map(int,open(0).read().split())
a,b,c = sorted([a,b,c])
while a+b <= c:
    c -= 1
print(a+b+c)