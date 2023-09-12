import sys
input = sys.stdin.readline
s = set()
for _ in range(int(input())):
    order = input().split()
    if order[0]=='add' and int(order[1]) not in s: s.add(int(order[1])); continue
    if order[0]=='remove' and int(order[1]) in s: s.remove(int(order[1])); continue
    if order[0]=='check': print(1 if int(order[1]) in s else 0); continue
    if order[0]=='toggle':
        if int(order[1]) in s: s.remove(int(order[1])); continue
        else : s.add(int(order[1])); continue
    if order[0]=='all': s=set(range(1,21)); continue
    if order[0]=='empty': s=set(); continue