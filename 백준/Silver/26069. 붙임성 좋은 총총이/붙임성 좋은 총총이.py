import sys
from collections import defaultdict
input = sys.stdin.readline
dic = defaultdict(int)
dic['ChongChong'] = 1
cnt = 1
for _ in range(int(input())):
    meet = input().split()
    if (dic[meet[0]]==1) or (dic[meet[-1]]==1):
        for m in meet:
            if not dic[m] :
                cnt += 1
                dic[m] = 1
                
print(sum(dic.values()))