N = int(input())

M = [[0]*10 for _ in range(10)]

for n in range(1,N+1):
    head = int(str(n)[0])
    tail = int(str(n)[-1])
    M[head][tail] += 1

ans = 0
for i in range(10):
    for j in range(i+1,10):
        ans += M[i][j]*M[j][i]*2
    ans += M[i][i]**2

print(ans)






