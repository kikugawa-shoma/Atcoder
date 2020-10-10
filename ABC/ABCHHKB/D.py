T = int(input())
N = [0]*T
A = [0]*T
B = [0]*T
for i in range(T):
    N[i], A[i], B[i] = map(int, input().split())

mod = 1000000007


def count(n, a, b):
    if n < a+b:
        return 0
    else:
