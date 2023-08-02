import sys
input = sys.stdin.readline
# n*n 행렬에서 전체가 다 같은 색인지 확인 후 아니면 4등분하는 함수
def division(n,paper,sum_paper):
    # 모두 같은 색인 경우
    if not sum_paper%(n**2) : # 전체 종이 색의 합을 n으로 나눈 나머지가 없다면 모두 같은 색
        ans[sum_paper//(n**2)] += 1 # 합이 0이면 하얀색+1, n**2이면 파란색+1
        
    # 4등분 해야하는 경우
    else :
        result_paper = [] # 모든 사분면을 담는 리스트
        result_sum = [] # 모든 사분면의 색의 합을 담는 리스트
        for row,col in [[0,0],[0,n//2],[n//2,0],[n//2,n//2]]: # 각 사분면 왼쪽 위 꼭지점
            quater_paper = [] # 사분면 중 1개
            quater_sum = 0 # 사분면 중 1개의 전체 합
            for i in range(n//2):
                quater_row = [] # 1개 사분면 중 1개 행
                for j in range(n//2):
                    quater_row.append(paper[row+i][col+j])
                quater_paper.append(quater_row) # 하나의 행이 완성되면 해당 사분면에 추가
                quater_sum += sum(quater_row) # 행의 합을 1개 사분면 전체 합에 추가
            result_paper.append(quater_paper) # 완성된 사분면 담기
            result_sum.append(quater_sum) # 완성된 사분면의 합 담기
        for new_paper,new_sum in zip(result_paper, result_sum): # 개별 사분면에 대해 해당 함수 재귀
            division(n//2,new_paper,new_sum) # 재귀 함수 진행 시 모두 같은 색일 경우 해당 함수 종료

ans = [0,0] # 흰색 개수, 파랑색 개수 최종 답안
paper = [] # 전체 종이
sum_paper = 0 # 전체 종이의 합
n = int(input())
for _ in range(n):
    row = list(map(int,input().split()))
    paper.append(row)
    sum_paper += sum(row)
division(n,paper,sum_paper)
for res in ans :
    print(res)