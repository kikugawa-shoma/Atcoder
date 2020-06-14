
N,Q = map(int,input().split())
A = [0]*(N+1)
B = [0]*(N+1)
C = [0]*Q
D = [0]*Q

en = [set() for i in range(1,2*10**5)]

for i in range(N):
    A[i+1],B[i+1] = map(int,input().split())
    en[A].add(B)
for i in range(Q):
    C[i],D[i] = map(int,input().split())
for i in range(Q):
    en
    


