import bisect as bc

N,M,K = map(int,input().split())
A = [0]*(N+1)
B = [0]*(M+1)
A[1:] = list(map(int,input().split()))
B[1:] = list(map(int,input().split()))
A.append(10**9+10)
B.append(10**9+10)

A_S = [0]*(N+2)
B_S = [0]*(M+2)

for i in range(1,N+2):
    A_S[i] = A_S[i-1]+A[i]
for i in range(1,M+2):
    B_S[i] = B_S[i-1]+B[i]

ans = 0
for i in range(N+2):
    tmp_K = K-A_S[i]
    if tmp_K > 0:
        j = bc.bisect_right(B_S,tmp_K) - 1
        ans = max(i+j,ans)
    if tmp_K == 0:
        ans = max(ans,i)
    
print(ans)






    


