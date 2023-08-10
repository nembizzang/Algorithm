import sys
input = sys.stdin.readline

def binary_search(q,n):
    sta,end = 0,n-1
    while sta <= end:
        mid = (sta+end)//2
        if nums[mid] == q: # 찾는 숫자를 발견했을 때
            return 1
        if nums[mid] < q : # 찾는 숫자가 중간보다 뒤에 있을 때
            sta = mid+1
        else : # 찾는 숫자가 중간보다 앞에 있을 때
            end = mid-1
    return 0

n = int(input())
nums = sorted(list(map(int,input().split())))
_ = input()
questions = list(map(int,input().split()))

for q in questions:
    print(binary_search(q,n))