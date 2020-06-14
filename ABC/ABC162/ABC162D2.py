import sys
A=[a.rstrip() for a in sys.stdin.readlines()]
N=int(A[0])
S="".join(["A",A[1]])

a=0
ans=S.count("R")*S.count("G")*S.count("B")

for i in range(1,N+1):
    for j in range(1,N+1):
        k=2*j-i
        if 1 <= k <= N and i < j < k:
            if S[i] != S[j] and S[j] != S[k] and S[k] != S[i]:
                ans -= 1
print(ans)

