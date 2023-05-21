import sys
input = sys.stdin.readline
cnt = 1
for i in range(2,int(input())+1):
    cnt *= i
print(cnt)