'''
1) n==1 이면 return [s]
2) s를 n으로 나눈 몫(t), 나머지(r)을 구하여 t가 s-r개, t+1이 r개 있는 list를 return
3) 몫이 0이면 return [-1]
'''
def solution(n, s):
    t,r = divmod(s,n)
    return [t]*(n-r)+[t+1]*r if t else [-1]