import sys
from collections import deque
input = sys.stdin.readline
n,k = map(int,input().split())
arrival = {i:0 for i in range(0,100001)} # 해당 지점 방문 여부
def bfs(cur,cnt): # 현재 위치와 이동 시간을 통해 다음 이동 위치를 정하는 bfs 함수 생성
    stack = deque()
    stack.append([cur,cnt])
    while stack:
        cur,cnt = stack.popleft()
        if cur == k :
            return cnt
        if arrival[cur]: # 이미 방문한 적이 있다면 통과
            continue
        arrival[cur] = 1
        cnt += 1
        # 0이면 +1만 가능 / 50001~99999 +1,-1만 가능 / 1~50000이면 셋 모두 가능 / 100000이면 -1만 가능
        if not cur:
            stack.append([cur+1,cnt])
        elif 1 <= cur <= 50000:
            stack.append([cur-1,cnt])
            stack.append([cur+1,cnt])
            stack.append([cur*2,cnt])
        elif 50001 <= cur <= 99999:
            stack.append([cur-1,cnt])
            stack.append([cur+1,cnt])
        else :
            stack.append([cur-1,cnt])
print(bfs(n,0))