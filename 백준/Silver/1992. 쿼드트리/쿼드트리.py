import sys
input = sys.stdin.readline
# 2차원 배열이 모두 같은 수인지 확인하고 아니면 4등분하는 함수
def division(n, sum_video, video):
    global ans
    if not sum_video%n**2 : # 모두 같은 수라면 나머지가 0이다.
        ans += f'{sum_video//n**2}'
    else :
        result_video, result_sum = [], [] # 4등분한 결과를 모두 담아줄 리스트
        for row,col in [[0,0],[0,n//2],[n//2,0],[n//2,n//2]]: # 사분면 왼쪽 위 좌표
            quater_video = [] # 해당 사분면 video를 담을 리스트
            quater_sum = 0 # 해당 사분면 sum을 담을 리스트
            for i in range(n//2):
                tmp_row = [] # 해당 사분면 중 각 행을 담을 리스트
                for j in range(n//2):
                    tmp = video[row+i][col+j] # 해당 칸의 값
                    tmp_row.append(tmp)
                    quater_sum += tmp
                quater_video.append(tmp_row) # 한개 행을 다돌고 해당 사분면에 추가
            # 한개 사분면이 완성되면 결과에 추가
            result_video.append(quater_video)
            result_sum.append(quater_sum)
        ans += '(' # 다음 레벨의 재귀함수로 넘어갈 때 괄호 열기
        for new_sum, new_video in zip(result_sum, result_video): # 사분면 별로 함수 실행
            division(n//2, new_sum, new_video) 
        ans += ')' # 해당 레벨의 재귀함수가 종료될 때 괄호 닫기
n = int(input().strip())
ans = ''
video = []
sum_video = 0
for _ in range(n):
    row = list(map(int,list(input().strip())))
    video.append(row)
    sum_video += sum(row)
division(n, sum_video, video)
print(ans)