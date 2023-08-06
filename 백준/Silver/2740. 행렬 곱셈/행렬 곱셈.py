import sys
input = sys.stdin.readline

n,m = map(int,input().split())
list_a = [list(map(int,input().split())) for _ in range(n)]
_,k = map(int,input().split()) # 행렬 곱셈이 가능하려면 a의 열과 b의 행이 같아야하기에 m 생략
list_b = [[] for _ in range(k)]
for _ in range(m):
    for i,num in enumerate(map(int,input().split())): # 각 행에 대해 행렬 전환
        list_b[i].append(num)
for i in range(n): # a의 행 하나씩 출력
    row = [] # 각 행의 연산 결과를 담아둘 리스트
    for j in range(k): # b의 행(실제는 열) 하나씩 출력
        row.append(sum([a*b for a,b in zip(list_a[i],list_b[j])])) # 행렬 곱 결과 하나씩 행에 담기
    print(*row)