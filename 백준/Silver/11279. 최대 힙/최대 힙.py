import sys
from heapq import heappush, heappop
input = sys.stdin.readline

nums = []
for _ in range(int(input())):
    i = int(input())
    if i :
        heappush(nums,-i)
    else :
        if not nums:
            print(0)
        else :
            print(-heappop(nums))