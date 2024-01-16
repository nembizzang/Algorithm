'''
빈 heap 자료구조를 두개 만든다.
삽입 연산은 heappush, 최소값 삭제 연산은 heappop을 사용한다.
최대값 삭제 연산은 원소가 하나 남을 때까지 최소값 삭제 연산을 함과 동시에 다른 빈 heap에 삽입 연산을 진행한 후
heap 두개의 이름을 변경해준다.
'''
from heapq import heapify, heappush, heappop
def solution(operations):
    heap1, heap2 = [],[]
    for op in operations:
        op, num = op.split()
        num = float(num)
        if op == 'I':
            heappush(heap1,num)
        else:
            if num == -1: # 최소값 삭제 연산
                if heap1: # 큐가 비어있지 않다면
                    heappop(heap1)
            else: # 최대값 삭제 연산
                while len(heap1) > 1 : # 하나 남을 때까지 heap1의 최소값을 heap2로 전달
                    heappush(heap2,heappop(heap1))
                heap1,heap2 = heap2,[] # heap1, heap2 서로 바꾸기
    if not heap1:
        return [0,0]
    if len(heap1)==1:
        return [heap1[0],heap1[0]]
    else :
        min_ = heappop(heap1)
        max_ = 0
        while heap1:
            max_ = heappop(heap1)
    return [max_,min_]