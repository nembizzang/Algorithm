import sys
input = sys.stdin.readline
nums = []
for _ in range(int(input())):
    order = input().split()
    if order[0] == 'push' :
        nums.append(int(order[1]))
    elif order[0] == 'pop' :
        try : print(nums.pop(0))
        except : print(-1)
    elif order[0] == 'size' :
        print(len(nums))
    elif order[0] == 'empty' :
        print(1 if not nums else 0)
    elif order[0] == 'front' :
        try : print(nums[0])
        except : print(-1)
    else :
        try : print(nums[-1])
        except : print(-1)