N,K=map(int, input().split())
mod=1000000007
A=[i for i in range(N+1)]
ans=0

S=[0]*(N+1)
for i in range(1,N+1):
    S[i]=S[i-1]+A[i]

for k in range(K,N+1):
    MIN=S[k-1]
    MAX=S[N]-S[N-k]
    ans+=(MAX-MIN+1)%mod
    ans%=mod
print(ans+1)
