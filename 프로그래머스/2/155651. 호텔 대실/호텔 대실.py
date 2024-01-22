'''
book_time을 ':'를 없애고 정수형태로 변경하고, 종료시간에 10분을 더한 후 heap 정렬한다.
end_times이라는 heap 구조를 생성
book_time에서 heappop으로 시작 시간이 가장 빠른 손님을 뽑는다.
최초 손님의 경우 : room_cnt+1, eet(earlist_end_time)에 퇴장 시간 넣어주고 end_times에 heappush 시작 시간
두번째 손님부터 :
earlist_end_time과 비교해서 그것보다 빠르면 room_cnt를 +1 해주고, eet에 더 빠른 퇴장시간으로 초기화
그것보다 느리면, end_times에 해당 손님의 종료 시각을 heappush, eet에 더 빠른 퇴장시간으로 초기화
'''
from heapq import heapify, heappush, heappop
def solution(book_time):
    new_book_time = []
    for sta,end in book_time: # book_time 정수 변환, 종료시간+10분(청소시간)
        sta = int(sta.replace(':',''))
        if int(end[-2:])>=50: # 50분 이상이면
            end = int(end.replace(':',''))+50 # 분을 60진법으로 나타내고 1시간 추가
        else :
            end = int(end.replace(':',''))+10
        new_book_time.append([sta,end])
    heapify(new_book_time)
    sta,end = heappop(new_book_time)
    eet = end # earlist_end_time
    room_cnt = 1
    end_times = []
    while new_book_time:
        sta,end = heappop(new_book_time)
        if eet > sta: # 가장 빠른 종료시간보다 현재 예약 시작시간이 빨라서 방 추가 필요
            room_cnt += 1
            min_,max_ = min(eet,end), max(eet,end)
            eet = min_ # 둘 중 더 빠른 종료시간으로 초기화
            heappush(end_times,max_) # 더 느린 종료시간은 end_times에 넣기
        else: # 방 추가 불필요
            heappush(end_times,end) # 이번 예약 종료시간 end_times에 추가
            eet = heappop(end_times) # 가장 빠른 퇴실시간 초기화
    print(room_cnt==len(end_times))
    return room_cnt