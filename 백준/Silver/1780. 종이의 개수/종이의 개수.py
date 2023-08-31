import sys
input = sys.stdin.readline

def dac(paper,len_set,n):
    if len_set == 1: # 종이의 원소 집합 길이가 1이라면
        ans[paper[0][0]] += 1
    else : # 그렇지 않다면 분할진행
        for i in range(0,n,n//3): # n=9일때, i=0,3,6
            for j in range(0,n,n//3): # n=9일때, j=0,3,6
                div_paper = [] # 한 구분면
                set_div_paper = set() # 한 구분면의 원소 집합
                for k in range(n//3): # n=9일때, k=0,1,2
                    row = paper[i+k][j:j+n//3] # 한 구분면의 한 행
                    div_paper.append(row)
                    set_div_paper = set_div_paper.union(set(row)) # 원소 집합 추가
                dac(div_paper,len(set_div_paper),n//3)
                
n = int(input())
paper = []
set_paper = set()
for _ in range(n):
    row = list(map(int,input().split()))
    set_paper = set_paper.union(set(row))
    paper.append(row)
ans = {-1:0,0:0,1:0}
dac(paper,len(set_paper),n)
for i in [-1,0,1]:
    print(ans[i])