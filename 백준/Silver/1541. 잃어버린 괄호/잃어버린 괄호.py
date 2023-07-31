import sys
input = sys.stdin.readline
num_op = ['('] # 문자열을 하나의 수나 연산자로 만들어 넣어줄 리스트
num = ''
for s in input().strip():
    if s not in ['+','-'] : # 연산자가 아닐 경우
        num += s # 숫자로 된 문자열에 숫자 추가
    else : # 연산자라면
        num_op.append(str(int(num))) # 숫자로 된 문자열이 완성되었으므로 맨 앞 0 떼고 추가
        op = ')-(' if s == '-' else '+'
        num_op.append(op)
        # 지금 연산자가 -라면 괄호를 닫아서 - 연산 숫자를 최대로 만들고 다시 괄호 시작
        # +라면 그대로 +만 넣기
        num = '' # num이 새로 시작되기에 ''으로 초기화
num_op.append(str(int(num))+')')# 마지막 수 넣어주기
print(eval(''.join(num_op)))
'''
num_op = [] # 문자열을 하나의 수나 연산자로 만들어 넣어줄 리스트
num = ''
for s in input().strip():
    if s not in ['+','-'] : # 연산자가 아닐 경우
        num += s # 숫자로 된 문자열에 숫자 추가
    else : # 연산자라면
        num_op.append(int(num)) # 숫자로 된 문자열이 완성되었으므로 맨 앞 0 떼고 추가
        op = ')-(' if s == '-' else '+'
        num_op.append(op)
        # 지금 연산자가 -라면 괄호를 닫아서 - 연산 숫자를 최대로 만들고 다시 괄호 시작
        # +라면 그대로 +만 넣기
        num = '' # num이 새로 시작되기에 ''으로 초기화
num_op.append(int(num)) # 마지막 수 넣어주기

ans = 0
tmp_num = 0
p_m = 1 # 최종답에 현재 괄호 수를 더할 때의 부호
for i in num_op: # )-(, +, 수 로 구성
    if i == ')-(' : # 괄호가 끝나고 새로운 괄호가 시작되면
        ans += tmp_num if p_m else -tmp_num # 처음 괄호라면 더해주고 아니면 빼준다.
        p_m = -1 # 첫번째 괄호가 아니면 전부 최종답에는 빼줄 것이다.
        tmp_num = 0 # 괄호 초기화
    elif type(i) == int : # 수라면
        tmp_num += i # 현재 괄호 안의 숫자 더하기
    # +라면 이 다음에는 무조건 수라서 그대로 진행
ans += p_m*tmp_num # 마지막 수도 연산해주기(-가 하나도 안나올 경우엔 더해야하기에 p_m을 곱하기)

print(ans)
'''