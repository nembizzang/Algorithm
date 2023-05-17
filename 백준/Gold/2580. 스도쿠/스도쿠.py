import sys
input = sys.stdin.readline

board = [] # input받은 sudoku 판
blank = [] # 빈 칸의 좌표를 담음
for i in range(9):
    board.append(list(map(int, input().split())))
    for j in range(9):
        if not board[i][j]:
            blank.append([i,j])
            
# 행 확인 함수: y행에 i가 있는지 확인(i가 빈 칸에 들어갈 수 있는지 확인)
def aivle_row(i,y):
    if i in board[y]:
        return False # 해당 행에 i가 있으므로 채우기 불가
    return True  

# 열 확인 함수: x열에 i가 있는지 확인(i가 빈 칸에 들어갈 수 있는지 확인)
def aivle_col(i,x):
    for k in range(9):
        if i == board[k][x]:
            return False # 해당 열에 i가 있으므로 채우기 불가
    return True  

# 블럭 확인 함수: 해당 블럭에 i가 있는지 확인
def aivle_block(i,y,x):
    block_y, block_x = 3*(y//3), 3*(x//3)
    for j in range(3):
        for k in range(3):
            if i == board[block_y+j][block_x+k]:
                return False # 해당 블록에 i가 있으므로 채우기 불가
    return True
    
def sudoku(n):
    if n == len(blank): # 모든 blank를 다 채웠다면(blank 하나 채울때마다 n이 커지기에)
        for row in board:
            print(*row)
        exit(0) # return으로 하면 모든 답을 다 뽑음 얘는 하나만 뽑고 끝   
    y,x = blank[n][0], blank[n][1] # 빈 칸 좌표
    for i in range(1,10):# 빈 칸에 숫자 넣기 가능인지 확인하여 해당 숫자로 일단 진행시켜
        if aivle_row(i,y) and aivle_col(i,x) and aivle_block(i,y,x): # 가능하다면
            board[y][x] = i # 빈 칸에 i 넣고
            sudoku(n+1) # 다음 빈 칸 찾아서 진행 --> 쭉 정답이라면 밑에 안가고 정답 출력하고 끝
            board[y][x] = 0 # 만약 빈 칸 채웠는데 그게 정답이 아니라면 다시 0으로 두고 for문 진행
            
sudoku(0)