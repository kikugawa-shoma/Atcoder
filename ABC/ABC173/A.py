N = int(input())
M = 1000
if N%M == 0:
    print(0)
else:
    print(M - N%M)