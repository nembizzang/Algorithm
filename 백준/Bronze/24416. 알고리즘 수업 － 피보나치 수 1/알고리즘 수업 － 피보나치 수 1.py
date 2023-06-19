# python 재귀함수 피보나치 수열
def fib(n) :
  if n <= 2 :
    return 1
  else :
    return fib(n-1) + fib(n-2)

# python DP 피보나치 수열
def fibonacci(n) :
  dp = [0] * (n+1)
  dp[1]=1
  dp[2]=1
  cnt = 0
  for i in range(3,n+1) :
     dp[i] = dp[i-2]+dp[i-1]
     cnt += 1
  return cnt

n = int(input())
print(f'{fib(n)} {fibonacci(n)}')