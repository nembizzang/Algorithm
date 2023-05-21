import sys
input = sys.stdin.readline
from collections import defaultdict

n,m = map(int,input().split())
dic = defaultdict(list)

for _ in range(n):
    word = input().split()[0]
    if len(word) < m:
        continue
    if not dic[word]:
        dic[word] += [-1,-len(word),word]
    else :
        dic[word][0] -= 1

for v in sorted(dic.values()):
    print(v[-1])