import sys
input = sys.stdin.readline
s = input().strip()
# k번째 자리까지의 a의 개수(0<=k<=len(s)) 배열
def count_a(a):
    cnts = [0]
    tmp_cnt = 0
    for i in s :
        if i == a:
            tmp_cnt += 1
        cnts.append(tmp_cnt)
    return cnts
# 검색할 알파벳에 따른 자리수 배열을 딕셔너리로 담아줌
alpha = {}
for _ in range(int(input())):
    a,sta,end = input().split()
    sta,end = int(sta),int(end)
    if a in alpha.keys(): # 이미 확인한 알파벳이라면
        cnts = alpha[a] # 자리수 배열을 만들 필요없이 딕셔너리에서 가져옴
        # end번째 자리까지의 a 개수 - sta-1번째 자리까지의 a 개수
        print(cnts[end+1]-cnts[sta]) # sta=3, end=6, s=bananas, a=a, cnts=[0,0,1,1,2,2,3,3]
    else : # 처음 보는 알파벳이라면
        cnts = count_a(a) # 자리수 배열 만들어줌
        print(cnts[end+1]-cnts[sta])
        alpha[a] = cnts # alpha 딕셔너리에 알파벳:자리수 배열 담아줌