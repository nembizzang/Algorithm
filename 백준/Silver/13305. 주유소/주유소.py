import sys
input = sys.stdin.readline
n = int(input())
# 시작할 때 주유하고, 기름을 넣은 주유소보다 기름값이 싼 주유소를 만나면 거기서 주유한다.
roads = list(map(int,input().split()))
costs = list(map(int,input().split()))[:-1] # 도착지점에서는 기름을 안넣으니 제외
tot_cost = 0 # 최종 전체 주유비
tmp_cost = costs[0] # 주유할 주유소에서의 비용, 첫번째 주유소에서 주유 후 시작
tmp_road = roads[0] # 다음 주유할 주유소까지의 거리, 두번째 도시까지 달릴만큼 넣어두고 시작
for road, cost in zip(roads[1:],costs[1:]):
    if tmp_cost > cost : # 현재 비용보다 싼 주유소를 만나면
        tot_cost += tmp_cost*tmp_road # 최종 전체 주유비에 현재 비용*이동거리 추가
        tmp_cost = cost # 현재 비용 초기화
        tmp_road = road # 지금 주유소에서 다음 도시까지 달릴만큼 넣어두고 시작
    else : # 현재 비용이 아직까지 최소비용이라면
        tmp_road += road # 다음 도시로의 이동 거리를 추가
tot_cost += tmp_cost*tmp_road # 마지막 주유비 추가
print(tot_cost)