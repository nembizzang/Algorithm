import sys
from itertools import permutations
def calc(a,b,oper):
    if oper == '+':
        return a+b
    elif oper == '-':
        return a-b
    elif oper == '*':
        return a*b
    else :
        if a*b < 0 :
            return -(abs(a)//abs(b))
        return a//b

n = int(input())
nums = list(map(int,input().split()))
op_amt = list(map(int,input().split()))
pmtd = ['+','-','*','/']

operation = []
for i in range(4):
    if op_amt[i] :
        operation += [pmtd[i]]*op_amt[i]

ans = []
for perm in permutations(operation,n-1):
    tmp = nums[0]
    for num,op in zip(nums[1:],perm):
        tmp = calc(tmp,num,op)
    ans.append(tmp)
print(max(ans))
print(min(ans))