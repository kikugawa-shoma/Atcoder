N, X = map(int, input().split())
L = list(map(int, input().split()))

D = [0] * (N + 1)

cnt = 0
for i in range(N):
    D[i+1] = D[i] + L[i]
    if D[i+1] <= X:
        cnt += 1

print(cnt + 1)
