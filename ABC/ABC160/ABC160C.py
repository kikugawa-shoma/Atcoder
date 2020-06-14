K, N = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

dis = [0]*N
for i in range(N-1):
    dis[i] = A[i+1] - A[i]

dis[N-1] = A[0] + K - A[N-1]

print(K-max(dis))


