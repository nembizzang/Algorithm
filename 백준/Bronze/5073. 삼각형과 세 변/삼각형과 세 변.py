import sys
input = sys.stdin.readline
while True :
    a,b,c = map(int,input().split())
    if a==0 :
        break
    a,b,c = sorted([a,b,c])
    if a+b <= c :
        print('Invalid')
    elif a==b :
        print('Equilateral' if b==c else 'Isosceles')
    else :
        print('Isosceles' if b==c else 'Scalene')