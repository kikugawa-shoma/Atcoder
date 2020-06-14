N,M,X = map(int,input().split())
C = [0]*N
A = [[0] for _ in range(N)]
for i in range(N):
    tmp = list(map(int,input().split()))
    C[i] = tmp[0]
    A[i] = tmp[1:M+1]
f = False
money_min = 100000000000
for i in range(1,2**N):
    use = format(i,"0{}b".format(N))
    money = 0
    understand = [0]*M
    for j in range(N):
        if use[j] == "1":
            money += C[j]
            for k in range(M):
                understand[k] += A[j][k]
    if min(understand) >= X and money < money_min:
        money_min = money
        f = True

if f:
    print(money_min)
else:
    print(-1)







