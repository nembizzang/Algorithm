import sys
input = sys.stdin.readline

def zearch(n,r,c):
    if n==0:
        return 0
    nr,rr = divmod(r,2)
    nc,rc = divmod(c,2)
    return 2*rr + rc + 4*zearch(n-1,nr,nc)
n,r,c = map(int,input().split())
print(zearch(n,r,c))