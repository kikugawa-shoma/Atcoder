N=int(input())
A=list(map(int, input().split()))
BOSS_NUM=[0]*(N+1)
for i in range(0,N-1):
    BOSS_NUM[A[i]]+=1

for i in range(N):
    print(BOSS_NUM[i+1])
