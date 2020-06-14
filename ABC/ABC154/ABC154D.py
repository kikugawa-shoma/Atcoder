N, K = map(int, input().split())
p = [int(a) for a in input().split()]

B = [0]*(N-K+1)
B[0] = sum(p[0:K])
for i in range(1, N-K+1):
    B[i] = B[i-1] - p[i-1] + p[i+K-1]

max_ind = B.index(max(B))

ep = 0
for i in range(K):
    ep += (p[max_ind+i]*(p[max_ind+i]+1))/(2*p[max_ind+i])

print(ep)

