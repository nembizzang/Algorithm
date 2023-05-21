import sys
input = sys.stdin.readline
def f(n) :
    if n <= 1:
        return 1
    return n*f(n-1)
print(f(int(input())))