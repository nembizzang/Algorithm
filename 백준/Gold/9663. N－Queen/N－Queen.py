import sys
input = sys.stdin.readline
n = int(input())
cnt = 0
board = [0]*n # n행에서 말들이 놓이는 열의 집합

# 해당 칸에 말을 두는 것이 가능한 지 출력
def aivle_block(y):
    for i in range(y): # 해당 행까지의 앞서 둔 말들의 열을 확인
        # 지금껏 둔 말들의 열과 내가 둘 곳의 열이 겹치지 않고, 대각선 방향으로도 겹치지 않으면 True
        if (board[i] == board[y]) or (abs(board[y]-board[i]) == abs(y-i)): # 절대값 열 간격 == 행 간격이면 대각선 위에
            return False
    return True

# 첫 행부터 한 칸 선택 -> 다음 행 진행 -> 한칸 선택 마지막 칸에 도착 및 선택 완료 시 1회 완료
def n_queen(y): # 한 행씩 진행
    global cnt
    if y == n: # n_queen 탈출 구문
        cnt += 1
    else: # dfs 구문
        for x in range(n): # 한 행 매 칸 마다 반복
            board[y] = x # y행 x열에 두겠다
            if aivle_block(y): # 해당 칸(x,y)에 두는 것이 가능하면
                n_queen(y+1) # 다음 행으로 진행시켜

n_queen(0)
print(cnt)