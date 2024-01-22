'''
words를 순환하며 각 단어끼리 알파벳 하나 차이만 나는 것들을 words_dict에 담아둔다.
begin부터 시작해서 words_dict의 word를 하나씩 꺼내서 bfs 진행
'''
from collections import defaultdict,deque
def solution(begin, target, words):
    def if_conn(word1, word2): # word1과 word2가 연결될 수 있는지 확인하는 함수
        cnt = 0
        for i,j in zip(word1,word2):
            if i != j :
                cnt += 1
        return True if cnt==1 else False
    
    # 변환 불가의 경우
    if target not in words:
        return 0
    
    # 간선 잇기
    words_dict = defaultdict(list)
    for i in range(len(words)):
        word = words[i]
        # begin에서 변환할 수 있는 word 찾기
        if if_conn(begin,word):
            words_dict[begin].append(word)
        # word에서 변환할 수 있는 단어 찾기
        for j in range(i+1,len(words)):
            vs_word = words[j]
            if if_conn(word,vs_word):
                words_dict[word].append(vs_word)
                words_dict[vs_word].append(word)

    # target과 이어진 간선이 없는 경우
    if not words_dict[target] and target not in words_dict[begin]:
        return 0
    
    # bfs
    stack = deque([[0,begin]])
    visited = {word:51 for word in words}
    while stack:
        cnt,tmp_word = stack.popleft()
        # 종료조건
        if tmp_word == target:
            return cnt
        # 순회
        for word in words_dict[tmp_word]:
            if visited[word] > cnt: # 가장 빠르게 방문한 경우라면
                stack.append([cnt+1,word])