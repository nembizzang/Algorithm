'''
야근피로도를 가장 줄이기 위해서는 가능한 모든 작업을 골고루 진행해서 최대값과 최소값의 차이를 줄여야한다.
works에 -를 붙이고 heap 정렬을 시킨다.
heappop으로 최대값을 뽑아내어 남은 것들 중 최대값보다 1이 작을때까지 일하기를 반복하자.
'''
from heapq import heapify, heappush, heappop
def solution(n, works):
    works = list(map(lambda x : -x, works))
    heapify(works)
    while n and len(works)>=2 : # 야근 시간이 남아있고 작업 종류가 2개 이상이라면
        a = heappop(works)
        b = works[0]
        if n < b-a+1: # 야근 시간이 최대값을 차대값-1까지 만들만큼 충분하지 않다면
            heappush(works,a+n) # a를 n만큼 일하고 heappush
            return sum(map(lambda x : x**2,works)) # 모든 일을 다했으므로
        n -= b-a+1 # 야근하기
        a = b+1
        if a: # a가 작업량이 남았다면(b가 1짜리 일인 경우)
            heappush(works,a)

    if n == 0 : # 작업 종류가 2개 이상인데 야근 시간이 없는 경우
        return sum(map(lambda x : x**2,works))
    # 야근 시간은 있는데 작업 종류가 1개인 경우
    a = works[0]
    return ((a+n)**2) if n < -a else 0