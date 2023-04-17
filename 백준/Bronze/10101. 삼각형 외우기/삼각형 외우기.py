x = list(map(int,open(0).read().split()))
a,b,c = sorted(x)
if sum(x) != 180 :
    print('Error')
elif a==60 :
    print('Equilateral')
elif (a!=b) & (b!=c) :
    print('Scalene')
else :
    print('Isosceles')