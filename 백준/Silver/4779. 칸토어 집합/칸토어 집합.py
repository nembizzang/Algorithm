nums = map(int,open(0).read().split())
def can(n,unit):
    if n == 3**num:
        return unit
    new_unit = ''
    for i in range(3):
        new_unit += unit if i != 1 else ' '*n
    return can(3*n,new_unit)

for num in nums:
    print(can(1,'-'))