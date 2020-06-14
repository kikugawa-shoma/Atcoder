N=int(input())
S=input()
R=[0]*N
G=[0]*N
B=[0]*N

for i in range(N):
    if S[i]=="R":
        R[i]=1
    elif S[i]=="G":
        G[i]=1
    else:
        B[i]=1
R_S=[0]*N
G_S=[0]*N
B_S=[0]*N
R_S[0] = R[0]
G_S[0] = G[0]
B_S[0] = B[0]
for i in range(1,N):
    R_S[i]=R_S[i-1]+R[i]
    G_S[i]=G_S[i-1]+G[i]
    B_S[i]=B_S[i-1]+B[i]

ans=0
for j in range(1,N-1):
    char=S[j]
    if char=="G":
        ans += R_S[j-1]*(B_S[N-1]-B_S[j])
        ans += B_S[j-1]*(R_S[N-1]-R_S[j])
        min_len=min(j,N-1-j)
        for i in range(1,min_len+1):
            if (S[j-i]=="R" and S[j+i]=="B") or (S[j-i]=="B" and S[j+i]=="R"):
                ans -= 1
    if char=="R":
        ans += G_S[j-1]*(B_S[N-1]-B_S[j])
        ans += B_S[j-1]*(G_S[N-1]-G_S[j])
        min_len=min(j,N-1-j)
        for i in range(1,min_len+1):
            if (S[j-i]=="G" and S[j+i]=="B") or (S[j-i]=="B" and S[j+i]=="G"):
                ans -= 1
    if char=="B":
        ans += G_S[j-1]*(R_S[N-1]-R_S[j])
        ans += R_S[j-1]*(G_S[N-1]-G_S[j])
        min_len=min(j,N-1-j)
        for i in range(1,min_len+1):
            if (S[j-i]=="G" and S[j+i]=="R") or (S[j-i]=="R" and S[j+i]=="G"):
                ans -= 1
print(ans)
        
            
