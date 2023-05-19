import sys
from itertools import combinations
input = sys.stdin.readline
aivle = []
tot = 0
n = int(input())
for _ in range(n):
    row = list(map(int,input().split()))
    aivle.append(row)
    tot += sum(row)
    
ans = 100*19*19
for team_1 in combinations(range(n),n//2):
    team_2 = list(set(range(n))-set(team_1))
    sco_1,sco_2 = 0,0
    for a, b in combinations(team_1,2):
        sco_1 += aivle[a][b] + aivle[b][a]
    for a, b in combinations(team_2,2):
        sco_2 += aivle[a][b] + aivle[b][a]
    if abs(sco_1-sco_2) < ans:
        ans = abs(sco_1-sco_2)
print(ans)