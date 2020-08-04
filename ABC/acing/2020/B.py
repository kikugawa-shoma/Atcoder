N = int(input())
A = list(map(int,input().split()))
A.insert(0,0)

ans = 0
for i in range(1,N+1):
    if i%2 == 1 and A[i] % 2 == 1:
        ans += 1

print(ans)
