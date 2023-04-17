a1,a0,c,n0 = map(int,open(0).read().split())
# f(n) = a1*n+a0
# g(n) = c*n, n >= n0
# n0 이상의 모든 n에 대하여, a1*n+a0 <= c*n인 양의 상수 c와 n0가 존재한다.
if c >= a1 :
    print(1 if (a0 <= (c-a1)*n0) else 0)
else :
    print(0)