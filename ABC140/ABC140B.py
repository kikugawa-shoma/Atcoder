N = int(input())
A = [int(a) for a in input().split()]
B = [int(a) for a in input().split()]
C = [int(a) for a in input().split()]

ans = sum(B)
pre_A = -1
for i in range(N):
    if pre_A + 1 == A[i]:
        ans += C[pre_A - 1]
    pre_A = A[i]

print(ans)

