N = int(input())
A = list(map(int,input().split()))
ans = 1
bind = 10**18

for i in range(N):
    if A[i] == 0:
        print(0)
        exit()

for i in range(N):
    ans*=A[i]
    if ans > bind:
        print(-1)
        exit()
print(ans)