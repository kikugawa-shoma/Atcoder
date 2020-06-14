N, X, Y = map(int, input().split())
dis_comb = [0]*N

for i in range(1, N):
    for j in range(i+1, N+1):
        dis_comb[min(abs(i-j), abs(X-i)+1+abs(Y-j))] += 1

for i in range(1, N):
    print(dis_comb[i])








