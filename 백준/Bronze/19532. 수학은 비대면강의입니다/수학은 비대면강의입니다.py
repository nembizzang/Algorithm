a,b,c,d,e,f = map(int,open(0).read().split())
print(*[(b*f-c*e)//(b*d-a*e), (c*d-a*f)//(b*d-a*e)])