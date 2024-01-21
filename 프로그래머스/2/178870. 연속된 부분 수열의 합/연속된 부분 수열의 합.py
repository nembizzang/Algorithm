'''
1) k보다 크면 작거나 같아질 때까지 첫 인덱스를 키워가며 누적합에 포함된 인덱스를 앞에서부터 줄인다.
2) k보다 작으면 작거나 같아질 때까지 끝 인덱스를 키워가며 누적합에 포함된 인덱스를 뒤로 늘린다.
3) 위 과정에서 해당 인덱스까지의 누적합이 k인 경우를 찾으면,
   기존 ans와 비교해서 전체 인덱스의 길이가 짧은 것을 정답을 초기화 시킨다.
   앞에서부터 뒤로 가며 비교할 것이기에 어차피 길이가 똑같은 것을 새로 발견했다면,
   기존의 ans가 먼저 시작하는 것이기에 굳이 첫 인덱스를 비교할 필요가 없다.
'''
def solution(sequence, k):
    ans = [0,len(sequence)-1] # 나중에는 부분수열의 첫,끝 인덱스를 담아줌
    # 합이 k인 부분 수열 찾기
    cur_sum = 0 # 현재 부분 수열의 합
    sta_idx = 0 # 부분 수열 시작 인덱스
    for end_idx in range(len(sequence)):
        cur_sum += sequence[end_idx]
        while sta_idx <= end_idx: # 첫 인덱스를 하나씩 키워가며 확인
            # k와 같은 경우
            if cur_sum == k and ans[1]-ans[0] > end_idx-sta_idx: # 더 짧은 부분 수열 확인
                ans = [sta_idx,end_idx] # 정답 초기화
                break # 끝 인덱스를 늘려서 다음 경우 확인
            # k보다 작은 경우
            if cur_sum < k:
                break # 끝 인덱스를 늘려서 다음 경우 확인
            # k보다 큰 경우
            cur_sum -= sequence[sta_idx] # 부분 수열 합 줄이기
            sta_idx += 1
            continue # 첫 인덱스를 늘려서 다음 경우 확인(while문 진행)         
    return ans