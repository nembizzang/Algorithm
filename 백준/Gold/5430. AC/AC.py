import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    str_f = input().strip()
    n,str_nums = int(input()), input().strip()
    # n==0이면 비어있는 리스트로(이래야 n==0이고 R만 있을 때 처리 가능)
    nums = deque(str_nums[1:-1].split(',')) if n else deque([])
    flag = True # 도중에 error가 없을 경우만 최종 결과 출력
    r_cnt = 0
    for function in str_f:
        if function == 'R' : # R이면 R 개수만 세주고 통과
            r_cnt += 1
        else : # D라면
            if not nums :
                print('error')
                flag = False
                break             
            if r_cnt%2 : # 그때까지 R의 개수가 홀수면 R 한번 진행 후 D 진행
                # R 실행 후 pop 해준 거니 pop
                nums.pop()
            else : # R 실행 없이 한 거니까
                nums.popleft()
    if flag :
        if r_cnt%2 : # 전체 R이 홀수라면 R 한번 진행
            nums.reverse()
        print('['+','.join(nums)+']')