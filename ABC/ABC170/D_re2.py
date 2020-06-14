import bisect as bc

N = int(input())
A = list(map(int,input().split()))
 
A.sort()
 
dp = [True for _ in range(A[-1]+1)]
finished = [False for _ in range(A[-1]+1)]
 

for i in range(N):
    if not finished[A[i]]:
        finished[A[i]] = True
        ai = A[i]
        for j in range(2,A[-1]+1):
            if ai*j > A[-1]:
                break
            dp[ai*j] = False

ans = 0
for i in range(N):
    if dp[A[i]]:
        if bc.bisect_right(A,A[i]) - bc.bisect_left(A,A[i]) == 1:
            ans += 1
 
print(ans)