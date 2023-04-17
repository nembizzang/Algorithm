import sys
from collections import defaultdict

input = sys.stdin.readline
employee = defaultdict(int)
for _ in range(int(input())) :
    name, _ = input().split()
    employee[name]+= -1 if employee[name] else 1
ans = []
for name in sorted(employee.keys()):
    if employee[name] :
        ans.append(name)
for name in sorted(ans, reverse=True):
    print(name)
    