import sys
input = sys.stdin.readline
s = input().strip()
def count_a(a):
    cnts = [0]
    tmp_cnt = 0
    for i in s :
        if i == a:
            tmp_cnt += 1
        cnts.append(tmp_cnt)
    return cnts
alpha = {}
for _ in range(int(input())):
    a,sta,end = input().split()
    sta,end = int(sta),int(end)
    if a in alpha.keys():
        cnts = alpha[a]
        print(cnts[end+1]-cnts[sta]) # sta=3, end=6, s=bananas, a=a, cnts=[0,0,1,1,2,2,3,3]
    else :
        cnts = count_a(a)
        print(cnts[end+1]-cnts[sta])
        alpha[a] = cnts