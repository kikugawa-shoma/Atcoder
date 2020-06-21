N = int(input())
A = list(map(int,input().split()))

S = 0
for a in A:
    S ^= a

B = [0]*N

for i in range(N):
    B[i] = S^A[i]
print(*B)




    