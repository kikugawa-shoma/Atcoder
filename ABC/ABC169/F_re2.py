import numpy as np

N,S = map(int,input().split())
A = list(map(int,input().split()))
coefs = np.array([0]*(S+1))
coefs[0] = 1

for i in range(N):
    tmp = coefs[:]
    coefs = coefs*2
    coefs[A[i]:] += tmp[:]
    
print(coefs[-1])
    

