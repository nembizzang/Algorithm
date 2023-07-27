import sys
from itertools import combinations
from collections import Counter
input = sys.stdin.readline
n,m = map(int,input().split())
nums = map(int,input().split())
# i번째 자리까지 합을 m으로 나눈 나머지(0<=i<=n)
rests = [0]
tmp_r = 0
for num in nums:
    tmp_r = (tmp_r+num)%m
    rests.append(tmp_r)
ans = 0
# rests에서 같은 숫자(나머지)를 두개 고르면 그 구간은 나머지가 0
for n in Counter(rests).values():
    ans += n*(n-1)//2 # 같은 숫자 n개 중에서 2개 조합의 수
print(ans)