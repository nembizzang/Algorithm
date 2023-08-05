import sys
input = sys.stdin.readline
a,b,c = map(int,input().split())
rests = [] # a**i의 나머지 집합
i = 1
rests.append(a%c)
# rests에는 a**1의 나머지, a**2의 나머지, a**4의 나머지, a**8의 나머지...가 들어간다.
while i <= b:
    rests.append((rests[-1]**2)%c)
    i *= 2
ans = 1
for rest,i in zip(rests,bin(b)[2:][::-1]): # b의 2진법을 뒤집었다.
    if int(i):
        ans = (ans*(rest*int(i))%c)%c
print(ans)