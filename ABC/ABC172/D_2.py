N = int(input())

divs = [0]*(N+1)

for i in range(1,N+1):
    for j in range(1,N+1):
        if i*j > N:
            break
        divs[i*j] += 1

ans = 0
for i in range(1,N+1):
    ans += i*divs[i]
print(ans)

