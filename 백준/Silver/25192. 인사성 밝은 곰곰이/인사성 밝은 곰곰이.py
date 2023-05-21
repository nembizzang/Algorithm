import sys
from collections import defaultdict
input = sys.stdin.readline
dic = defaultdict(int)
cnt = 0
for _ in range(int(input())):
    name = input().strip()
    if name == 'ENTER':
        del dic
        dic = defaultdict(int)
        continue
    if not dic[name]:
        dic[name]+=1
        cnt += 1
        
print(cnt)