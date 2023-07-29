import sys
input = sys.stdin.readline
n,k = map(int,input().split())
coins = []
for _ in range(n):
    coin = int(input())
    if coin <= k :
        coins.append(coin)
    else :
        continue # k원보다 큰 코인은 coins 배열에 넣지 않는다.
coins = sorted(coins,reverse=True) # coins 내림차순 정렬
ans = 0
for coin in coins: # 제일 큰 코인부터 꺼내면서 
    cnt,k = divmod(k,coin) # cnt는 몫으로 코인 개수 / k는 나머지로 초기화
    ans += cnt # ans에 코인 개수 추가
    if not k : # 필요 금액을 다 채웠다면
        print(ans)
        break
        