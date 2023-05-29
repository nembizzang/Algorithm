import sys
input = sys.stdin.readline
n = int(input())
town = []
for _ in range(n):
    town.append(list(map(int,list(input().strip()))))
ans = []
def dfs(y,x):
    global v_cnt
    town[y][x] = 0 # 확인했으니 집 파괴
    for dy,dx in [[-1,0],[1,0],[0,-1],[0,1]]: # 상,하,좌,우의 좌표로 이동
        ny,nx = y+dy, x+dx
        # 좌표가 마을 범위 안에 있고(0~n-1), 거기 집이 있다면
        if (0<=ny<n) & (0<=nx<n):
            if town[ny][nx]:
                v_cnt += 1
                dfs(ny,nx)
for y in range(n):
    for x in range(n):
        if town[y][x] :
            v_cnt = 1
            dfs(y,x)
            ans.append(v_cnt)
ans.sort()
print(len(ans))
for a in ans:
    print(a)