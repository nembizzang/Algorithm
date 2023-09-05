import sys
input = sys.stdin.readline
from collections import defaultdict, deque
n = int(input())
weights = deque(list(map(int,input().split())))
cn = int(input())
cweights = deque(list(map(int,input().split())))
dp = defaultdict(int)
dp[0] = 0
while weights:
    w = weights.popleft()
    key_list = list(dp.keys())
    for key in key_list :
        dp[key+w] = dp[abs(key-w)] = 1
ans = ''
while cweights :
    cw = cweights.popleft()
    ans += 'Y ' if dp[cw] else 'N '
print(ans[:-1])